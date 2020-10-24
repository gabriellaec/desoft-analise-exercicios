def estritamente_crescente(lista):
    i=0
    resposta=[]
    maior=lista[0]
    while i < len(lista):
        if lista[i] > maior:
        resposta.append(lista[i])
        i+=1
    return resposta
numeros=[0,2,2,3,5,6,8]
print(estritamente_crescente(numeros))