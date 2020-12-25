# dict-logic
## Usage
### Basic
```python
from dictlogic import Logic

logic = Logic()
result = logic.run({
    'sequence': [
        {'print': 'hello world!'},
        {'set': ['a', 10]},
        {'print': ['the value of a is', {'get': 'a'}]},
        {'select': [
            {'>': [{'get': 'a'}, 5]},
            {'print': 'this expression will be evaluated'},
            {'print': 'this expression will be ignored'},
        ]},
        {'set': ['a', {'*': [{'get': 'a'}, 2]}]},
        {'get': 'a'},
    ],
})
assert(result == 20)
```

### With given local variabls
```python
from dictlogic import Logic

logic = Logic()
result = logic.run({
    'sequence': [
        {'print': ['the value of a is', {'get': 'a'}]},
        {'set': ['c', {'+': [{'get': 'a'}, {'get': 'b'}]}]},
        {'print': ['the value of c is', {'get': 'c'}]},
    ],
}, {
    'a': 5,
    'b': 3,
})
```

### With custom functions
```python
from dictlogic import Logic

logic = Logic()

@logic.add('sqrt')
def sqrt(x):
    return x() ** 0.5

@logic.add('mean')
def power(*args):
    args = [arg() for arg in args]
    return sum(args) / len(args)


logic.run({'print': {'sqrt': 2}})
logic.run({'print': {'mean': [1, 2, 3, 4, 5, 6, 7]}})
```