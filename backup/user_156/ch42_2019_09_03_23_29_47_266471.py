import collections
def quantos_uns(x):
    repetidos = collections.Counter(input(x))
    return(repetidos[1])
    