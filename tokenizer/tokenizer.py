import re


def tokenizer(string: str):
    token_rexes = [
        (re.compile(r"^[a-zA-Z_]\w*"), "identifier"),  # variables
        (re.compile(r"^\d+"), "number"),  # integers
        (re.compile(r"^\d[.]\d*"), "decimal"),  # floats
        (re.compile(r'^"[a-zA-Z_]\w*"'), "word"),  # strings
        (re.compile(r"^[+*/-]"), "operator"),  # operators
        (re.compile(r"^[()]"), "parentheses"),  # parentheses
        (re.compile(r"^[{}]"), "braces"),  # braces
        (re.compile(r"^="), "assignment")  # assignment
    ]

    tokens = []

    while len(string):
        string = string.lstrip()

        matched = False

        for token_rex, token_type in token_rexes:
            mo = token_rex.match(string)
            if mo:
                matched = True
                token = (mo.group(0), token_type)
                tokens.append(token)
                string = token_rex.sub('', string)
                break

        if not matched:
            raise Exception("Invalid String")

    return tokens
