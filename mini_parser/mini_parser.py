from .symbol_table import SymbolTable


def parse_assignment(tokens: list):
    name = tokens[0][0]
    value = tokens[2:]
    value = parse_expression(value)
    SymbolTable.add_symbol(name, value)


def parse_expression(tokens: list):
    # Shunting Yard algorithm
    operator_stack = []
    expression_stack = []

    tokens.append( (')', "parentheses") )

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token[0] == "(":
            value, tokens = parse_expression(tokens[i+1:])
            expression_stack.append(value)

        elif token[1] == "num":
            expression_stack.append(token[0])

        elif token[1] == "var":
            pass

        elif token[1] == "operator":
            pass

        elif token[0] == ")":
            pass



def mini_parser(tokens: list):
    # assignment statement
    if tokens[1][0] == "=":
        parse_assignment(tokens)
    else:  #expressions
        parse_expression(tokens)

