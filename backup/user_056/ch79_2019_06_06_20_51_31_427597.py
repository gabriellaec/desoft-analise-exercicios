
def monta_dicionario(lista1,lista2):
    dicionario={}
    for numero in range(0,len(lista1)):
        if not lista1[numero] in dicionario:
            dicionario[lista1[numero]]=[lista2[numero]]
        else:
            dicionario[lista1[numero]].append(lista2[nunmero])
    return dicionario