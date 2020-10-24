from functools import reduce
def soma_impares(l):
    impares = list(filter(lambda x: x%2 != 0))
    return reduce(lambda x, y: x+y, impares)