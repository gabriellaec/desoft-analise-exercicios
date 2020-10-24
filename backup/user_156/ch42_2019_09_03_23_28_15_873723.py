import collections
def quantos_uns(x):
    repetidos = collections.Counter(x)
    return(repetidos[1])
    