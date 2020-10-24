def subtracao_de_listas(a,b):
    retorno = [x for ia in a if ia not in b]
    print(a,b,retorno)
    return retorno