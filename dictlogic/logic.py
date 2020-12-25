from .scope import create_scope
from .types import Function, Primitive
from .utils import aslist


class Logic:
    def __init__(self):
        self.globals = {}

    def run(self, statement, locals=None):
        with create_scope(self.globals) as scope:
            scope.locals = locals if locals is not None else {}
            return self.evaluate(statement)()

    def evaluate(self, statement):
        if self.is_primitive(statement):
            return Primitive(statement)
        elif self.is_function(statement):
            name, parameters = list(statement.items())[0]
            expression = Function(
                name, [self.evaluate(parameter) for parameter in aslist(parameters)])
            return expression

    def add(self, name):
        def decorator(func):
            self.globals[name] = func
            return func
        return decorator

    @staticmethod
    def is_primitive(value):
        return not isinstance(value, dict)

    @staticmethod
    def is_function(value):
        return isinstance(value, dict)