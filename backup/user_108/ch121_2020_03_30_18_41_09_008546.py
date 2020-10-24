def subtracao_de_listas(a,b):
    return (filter(lambda item: not item in b,a))
    