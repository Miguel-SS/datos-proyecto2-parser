from .symbol_table import SymbolTable
from .model.symbol import Symbol

scopes_stack = []
errors_list = []
line_counter = 0


def parse_declaration(tokens: list):
    name = tokens[1][0]
    value = Symbol(tokens[0][0], name, None, line_counter, scopes_stack[-1])
    SymbolTable.add_symbol(name, value)


def parse_assignment(tokens: list):
    name = tokens[0][0]
    value = Symbol(tokens[2][1], name, tokens[2][0], line_counter, scopes_stack[-1])
    if SymbolTable.find_symbol(name).get_type() == value.get_type():
        SymbolTable.add_symbol(name, value)
    else:
        error = 'Error linea ' + str(line_counter) + ': "' + name + '" parametro incorrecto - se esperaba (' + \
                value.get_type() + ')'
        errors_list.append(error)
        # print('Error linea x: "' + name + '" parametro incorrecto - se esperaba (' + value.get_type() + ')')


def parse_assign_declaration(tokens: list):
    name = tokens[1][0]
    val_symbol = SymbolTable.find_symbol(tokens[3][0])
    if val_symbol is not None:
        value = Symbol(val_symbol.get_type(), name, val_symbol.get_value(), line_counter, scopes_stack[-1])
        if tokens[0][0] == value.get_type():
            SymbolTable.add_symbol(name, value)
        else:
            error = 'Error linea ' + str(line_counter) + ': Asignacion incorrecta ' + val_symbol.get_name() + ' (' + val_symbol.get_type() + \
                    ') a ' + name + ' (' + tokens[0][0] + ')'
            errors_list.append(error)
            # print('Error linea x: Asignacion incorrecta ' + val_symbol.get_name() + ' (' + val_symbol.get_type() + ') a ' + name + ' (' + tokens[0][0] + ')')
    else:
        value = Symbol(tokens[3][1], name, tokens[3][0], line_counter, scopes_stack[-1])
        if tokens[0][0] == value.get_type():
            SymbolTable.add_symbol(name, value)
        else:
            error = 'Error linea ' + str(line_counter) + ': Asignacion incorrecta ' + tokens[3][0] + ' (' + tokens[3][1] + ') a' + name + ' (' \
                    + tokens[0][0] + ')'
            errors_list.append(error)
            # print('Error linea x: Asignacion incorrecta ' + tokens[3][0] + ' (' + tokens[3][1] + ') a' + name + ' (' + tokens[0][0] + ')')


def parse_function(tokens: list):
    i = 3
    scopes_stack.append('local_' + tokens[1][0])
    while tokens[i][0] != ')':
        token = [tokens[i], tokens[i+1]]
        parse_declaration(token)
        if tokens[i+2][0] == ',':
            i = i+1
        i = i+2

    name = tokens[1][0]
    value = Symbol(tokens[0][0], name, None, line_counter, 'global')
    SymbolTable.add_symbol(name, value)


def parse_return(tokens: list):
    if tokens[1][1] == 'identifier':
        value = SymbolTable.find_symbol(tokens[1][0])
        val_function = SymbolTable.find_symbol(value.get_field()[6:])
        if value.get_type() == val_function.get_type():
            val_function.set_value(value.get_value)
        else:
            error = 'Error linea ' + str(line_counter) + ': Valor de retorno (' + value.get_type() + \
                    ') no coincide con el valor de retorno de la funcion (' \
                    + val_function.get_type() + ')'
            errors_list.append(error)

    elif (tokens[1][1] == 'string') or (tokens[1][1] == 'float') or (tokens[1][1] == 'int'):
        val_function = SymbolTable.find_symbol(scopes_stack[-1][6:])
        if tokens[1][1] == val_function.get_type():
            val_function.set_value(tokens[1][0])
        else:
            error = 'Error linea ' + str(line_counter) + ': Valor de retorno (' + tokens[1][1] + \
                    ') no coincide con el valor de retorno de la funcion (' + \
                    val_function.get_type() + ')'
            errors_list.append(error)


def parse_conditional(tokens: list):
    name_flag = scopes_stack[-1][scopes_stack[-1].find('_') + 1:]
    scopes_stack.append('if_' + name_flag)
    val_1 = None
    val_2 = None
    if tokens[2][1] == 'identifier':
        val_1 = SymbolTable.find_symbol(tokens[2][0]).get_type()
    elif (tokens[2][1] == 'float') or (tokens[2][1] == 'string') or (tokens[2][1] == 'int'):
        val_1 = tokens[2][1]

    if tokens[4][1] == 'identifier':
        val_2 = SymbolTable.find_symbol(tokens[4][0]).get_type()
    elif (tokens[4][1] == 'float') or (tokens[4][1] == 'string') or (tokens[4][1] == 'int'):
        val_2 = tokens[4][1]

    if val_1 != val_2:
        error = 'Error en la linea ' + str(line_counter) + ': Comparacion de (' + val_1 + ') con (' + val_2 + ')'
        errors_list.append(error)
    if tokens[3][1] != 'equals':
        error = 'Error en la linea ' + str(line_counter) + ': Signo incorrecto, no es de comparacion'
        errors_list.append(error)


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
        if scopes_stack[-1] != 'global':
            scopes_stack.pop()
    else:
        print('ERROR')


def mini_parser(lines: list):
    scopes_stack.append('global')
    global line_counter
    for line in lines:
        line_counter = line_counter + 1
        if line[0][1] != 'empty':
            line_parser(line)

    if len(errors_list) > 0:
        for error in errors_list:
            print(error)
    else:
        print('BUILD SUCCESS')
