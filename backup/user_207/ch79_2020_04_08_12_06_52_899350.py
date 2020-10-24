dicionario ={}
def monta_dicionario (lista_A, lista_B):
    i=0
    while i< len(lista_B):
        dicionario[lista_A[i]] = lista_B[i]
        i+=1

    return dicionario