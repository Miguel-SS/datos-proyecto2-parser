from tokenizer import tokenizer
from mini_parser import mini_parser

# author Miguel Sanchez Salas
# author Daniel Ulloa Rojas

print("Mini Interpreter\n")

fic = open('incorrecto.txt', "r")
lines = []

for line in fic:
    lines.append(tokenizer(line))
mini_parser(lines)

