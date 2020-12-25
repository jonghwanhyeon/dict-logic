import functools
from .scope import current_scope


namespace = {
    '>': lambda x, y: x() > y(),
    '>=': lambda x, y: x() >= y(),
    '<': lambda x, y: x() < y(),
    '<=': lambda x, y: x() <= y(),
    '==': lambda x, y: x() == y(),
    '!=': lambda x, y: x() != y(),
    '+': lambda *args: functools.reduce(lambda x, y: x() + y(), args),
    '-': lambda *args: functools.reduce(lambda x, y: x() - y(), args),
    '*': lambda *args: functools.reduce(lambda x, y: x() * y(), args),
    '/': lambda *args: functools.reduce(lambda x, y: x() / y(), args),
    'and': lambda *args: functools.reduce(lambda x, y: x() and y(), args),
    'or': lambda *args: functools.reduce(lambda x, y: x() or y(), args),
}

def add(name):
    def decorator(func):
        namespace[name] = func
        return func
    return decorator

@add('sequence')
def sequence(*expressions):
    for expression in expressions:
        result = expression()
    return result

@add('select')
def select(condition, then, otherwise=None):
    if condition():
        return then()
    else:
        if otherwise is not None:
            return otherwise()
    return None

@add('get')
def get(name):
    return current_scope().resolve(name())

@add('set')
def set(name, value):
    namespace = current_scope().namespace(name())
    if namespace is None:
        namespace = current_scope().locals
    
    namespace[name()] = value()

@add('getitem')
def getitem(sequence, index):
    return sequence()[index()]

@add('print')
def print_(*args):
    args = [arg() for arg in args]
    return print(*args, flush=True)