from .symbol_table import SymbolTable


def parse_declaration(tokens: list):
    name = tokens[1][0]
    value = (None, tokens[0][0])
    SymbolTable.add_symbol(name, value)
    print(SymbolTable.symbols)


def parse_assignment(tokens: list):
    name = tokens[0][0]
    value = tokens[2]
    if SymbolTable.find_symbol(name)[1] == value[1]:
        SymbolTable.add_symbol(name, value)
        print(SymbolTable.symbols)
    else:
        print("Tipo de dato no coincide")


def parse_assign_declaration(tokens: list):
    if tokens[0][0] == tokens[3][1]:
        name = tokens[1][0]
        value = tokens[3]
        SymbolTable.add_symbol(name, value)
        print(SymbolTable.symbols)
    else:
        print("Tipo de dato no coincide con la declaracion")


def parse_function(tokens: list):
    i = 3
    while tokens[i][0] != '{':
        token = [tokens[i], tokens[i+1]]
        parse_declaration(token)
        if tokens[i+2][0] == ')':
            break
        elif tokens[i+2][0] == ',':
            i = i+1
        i = i+2


def parse_conditional(tokens: list):
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
        else:
            if tokens[1][1] == 'assignment':
                parse_assignment(tokens)
    else:
        print('ERROR')


def mini_parser(lines: list):
    for line in lines:
        line_parser(line)




