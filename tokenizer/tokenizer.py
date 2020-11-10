import re

def tokenizer(string: str):
    token_rexes = [
        re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*"),  # variables
        re.compile(r"[0-9]+"),  # integers
        re.compile(r"[+*/-]"),  # operators
        re.compile(r"[()]"),  # parentheses
        re.compile(r"[=]")  # assignment
    ]

    tokens = []

    while len(string):
        string = string.lstrip()

        for token_rex in token_rexes:
            mo = token_rex.match(string)
            if mo:
                token = mo.group(0)
                tokens.append(token)
                string = token_rex
