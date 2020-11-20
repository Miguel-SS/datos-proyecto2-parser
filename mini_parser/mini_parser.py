from .symbol_table import SymbolTable
from .model.symbol import Symbol

stack_flags = []


def parse_declaration(tokens: list):
    name = tokens[1][0]
    # value = (None, tokens[0][0])
    value = Symbol(tokens[0][0], name, None, 1, stack_flags[-1])
    SymbolTable.add_symbol(name, value)
    # print(SymbolTable.symbols)


def parse_assignment(tokens: list):
    name = tokens[0][0]
    # value = tokens[2]
    value = Symbol(tokens[2][1], name, tokens[2][0], 1, stack_flags[-1])
    if SymbolTable.find_symbol(name).get_type() == value.get_type():
        SymbolTable.add_symbol(name, value)
        # print(SymbolTable.symbols)
    else:
        print('Error linea x: "' + name + '" parametro incorrecto - se esperaba (' + value.get_type() + ')')


def parse_assign_declaration(tokens: list):
    name = tokens[1][0]
    # value = tokens[3]
    val_symbol = SymbolTable.find_symbol(tokens[3][0])
    if val_symbol is not None:
        value = Symbol(val_symbol.get_type(), name, val_symbol.get_value(), 1, stack_flags[-1])
    else:
        value = Symbol(tokens[3][1], name, tokens[3][0], 1, stack_flags[-1])
    if tokens[0][0] == value.get_type():
        SymbolTable.add_symbol(name, value)
        # print(SymbolTable.symbols)
    else:
        print('Error linea x: "' + name + '" parametro incorrecto - se esperaba (' + value.get_type() + ')')


def parse_function(tokens: list):
    i = 3
    stack_flags.append('local_' + tokens[1][0])
    while tokens[i][0] != ')':
        token = [tokens[i], tokens[i+1]]
        parse_declaration(token)
        # if tokens[i+2][0] == ')':
        #     break
        if tokens[i+2][0] == ',':
            i = i+1
        i = i+2


def parse_return(tokens: list):
    pass


def parse_body(lines: list):
    for line in lines:
        if line[0][0] == '}':
            break


def parse_conditional(tokens: list):
    pass


def call_function(tokens: list):
    pass


def line_parser(tokens: list):

    if tokens[0][1] == 'identifier':
        if (tokens[0][0] == 'void') or (tokens[0][0] == 'string') or (tokens[0][0] == 'int') or (tokens[0][0] == 'float'):
            if len(tokens) < 3:
                parse_declaration(tokens)
            elif tokens[2][0] == '(':
                parse_function(tokens)
            else:
                parse_assign_declaration(tokens)
        elif (tokens[0][0] == 'if') or (tokens[0][0] == 'while'):
            parse_conditional(tokens)
        elif tokens[0][0] == 'return':
            parse_return(tokens)
        else:
            if tokens[1][1] == 'assignment':
                parse_assignment(tokens)
            elif tokens[1][0] == '(':
                call_function(tokens)
    elif tokens[0][0] == '}':
        if stack_flags[-1] != 'global':
            stack_flags.pop()
    else:
        print('ERROR')


def mini_parser(lines: list):
    stack_flags.append('global')
    for line in lines:
        if line[0][1] != 'empty':
            line_parser(line)

