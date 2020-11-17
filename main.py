
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
# (1 + (2 - 3) * 4 / 5) + "abc"


# from mini_parser.symbol_table import SymbolTable
#
# SymbolTable.add_symbol("a", 10)
# SymbolTable.add_symbol("b", 40)
# SymbolTable.add_symbol("c", 139)
# SymbolTable.add_symbol("a", 2)
#
# print(SymbolTable.find_symbol("r"))
#
# print(SymbolTable.symbols)
