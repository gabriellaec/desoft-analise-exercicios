def subtracao_de_listas (listaA, listaB):
    i=0
    j=0
    listaC =[]
    while j<len(listaB):
        while i<len(listaA):
            if listaA[i] != listaB[j]:
                listaC.append(listaA[i])
            i += 1
        j+=1
    return listaC

print (subtracao_de_listas (listaA, listaB))