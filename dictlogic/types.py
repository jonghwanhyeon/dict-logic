from .scope import current_scope


class Function:
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters
        self.evaluated = False

    def __call__(self):
        if not self.evaluated:
            self.value = current_scope().resolve(self.name)(*self.parameters)
            self.evaluated = True
        return self.value

    def __repr__(self):
        return f'{self.name}(' \
            f'{", ".join(repr(parameter) for parameter in self.parameters)})'

class Primitive:
    def __init__(self, value):
        self.value = value

    def __call__(self):
        return self.value

    def __repr__(self):
        return repr(self.value)