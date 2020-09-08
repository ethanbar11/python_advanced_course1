def a(lst):
    return list(map(lambda x: x * 2, lst))


def b(lst):
    evens_amount = len(list(filter(lambda x: x % 2 == 0, lst)))
    odds_amount = len(lst) - evens_amount
    return (evens_amount, odds_amount)


def c(dictio):
    x = next(filter(lambda k, v: isinstance(v, str), dictio))
    pass


lst = [1, 2, 3, 4, 5]
dictio = {'a': 5, 'b': 3, 'c': 'bla bla'}
print(a(lst))
print(b(lst))
print(c(dictio))
