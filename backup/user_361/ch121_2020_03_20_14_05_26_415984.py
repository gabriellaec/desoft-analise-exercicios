def subtracao_de_listas(a,b):
    retorno = [x for x in a if x not in b]
    print(a,b,retorno)
    return retorno