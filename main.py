from tokenizer import tokenizer
# import mini_parser

print("Mini Interpreter\n")

while True:
    try:

        input_ = input(">> ")

        # tokenize
        tokens = tokenizer(input_)

        # parse

        print("Tokens: ", tokens)
    except KeyboardInterrupt:
        exit()


# Tests:
# 1 + 2 - 3 * 4 / 5
# (1 + 2 - 3 * 4 / 5)
# 1 + (2 - 3) * 4 / 5
# (1 + (2 - 3) * 4 / 5)

