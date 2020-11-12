
def parse_assignment(tokens: list):
    pass


def parse_expression(tokens: list):
    pass


def mini_parser(tokens: list):
    # assignment statement
    if tokens[1] == "=":
        parse_assignment(tokens)
    else:  #expressions
        parse_expression(tokens)

