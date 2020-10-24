dicionario = dict()
def monta_dicionario(listaA, listaB):
    i = 0
    for a in range(listaA):
        dicionario[i] = a
   
    for b in range(listaB):
        i = listaB[i]
        i += 1
    
    