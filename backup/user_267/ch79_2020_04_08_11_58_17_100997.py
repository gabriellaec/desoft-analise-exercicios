
def monta_dicionario(listaA, listaB):
    dicionario = dict()
    i = 0
    for a in listaA:
        dicionario[a] = listaB[i]
        i += 1
    return dicionario
    
    