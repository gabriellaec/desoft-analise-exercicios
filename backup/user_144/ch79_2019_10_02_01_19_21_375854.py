dic = {}
def monta_dicionario(lista1,lista2):
    for numero in range(len(lista1)):
        dic[lista1[numero]] = lista2[numero]
    return dic