dicionario = dict()
def monta_dicionario(listaA, listaB):
    i = 0
    for a in listaA:
        dicionario[i] = a
    for b in listaB:
        i = listaB[i]
        i += 1
    return dicionario
    
    