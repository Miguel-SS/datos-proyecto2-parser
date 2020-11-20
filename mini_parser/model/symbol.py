

class Symbol:

    def __init__(self, type_, name_, value_, line_, field_):
        self.type = type_
        self.name = name_
        self.value = value_
        self.line = line_
        self.field = field_
        self.parameters = []

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_line(self):
        return self.line

    def get_field(self):
        return self.field

    def get_parameters(self):
        return self.parameters

    def set_value(self, _value):
        self.value = _value

    def __str__(self):
        return self.type + "/" + self.name + "/" + str(self.value) + "/" + str(self.line) + "/" + self.field

