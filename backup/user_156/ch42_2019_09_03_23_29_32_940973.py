import collections
def quantos_uns(x):
    repetidos = collections.Counter(int(x))
    return(repetidos[1])
    