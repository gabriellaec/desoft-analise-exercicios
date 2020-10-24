def subtracao_de_listas(a,b):
    return list(filter(lambda item: not item in b,a))
