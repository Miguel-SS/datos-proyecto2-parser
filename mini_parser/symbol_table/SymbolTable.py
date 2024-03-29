from ..model.symbol import Symbol


class SymbolTable:
    symbols = dict()

    @staticmethod
    def add_symbol(name, value: Symbol):
        for key in SymbolTable.symbols:
            if key == name:
                SymbolTable.symbols[key] = value
                return

        SymbolTable.symbols[name] = value

    @staticmethod
    def find_symbol(name):
        for key in SymbolTable.symbols:
            if key == name:
                return SymbolTable.symbols[key]
        return None


