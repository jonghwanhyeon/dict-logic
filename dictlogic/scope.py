from contextlib import contextmanager


scopes = []

class Scope:
    def __init__(self, globals=None):
        from .builtins import namespace as builtins
        self.namespaces = [
            globals if globals is not None else {},
            builtins,
        ]
        self.locals = {}

    def namespace(self, name):
        namespaces = [
            self.locals if self.locals is not None else {},
            *self.namespaces,
        ]
        for namespace in namespaces:
            if name in namespace:
                return namespace
        return None

    def resolve(self, name):
        namespace = self.namespace(name)
        if namespace is None:
            return None
        return namespace[name]

def push_scope(globals):
    scopes.append(Scope(globals))

def pop_scope():
    scopes.pop()

def current_scope():
    return scopes[-1]

@contextmanager
def create_scope(globals):
    push_scope(globals)
    yield current_scope()
    pop_scope()