dicionario = dict()
def monta_dicionario(listaA, listaB):
    i = 0
    e = 0
    for a in listaA:
        dicionario[i] = a
    for b in listaB:
        i = listaB[e]
        i += 1
        e += 1
    return dicionario
    
    