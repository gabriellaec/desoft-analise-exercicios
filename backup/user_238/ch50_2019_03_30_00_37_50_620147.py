def numero_no_indice(lista):
    i=0
    resposta=[]
    while i < len(lista):
        if lista[i] == i:
            resposta.append(i)
        i+=1
    return resposta
numeros=[0,2,2,3,5,6,8]
print(numero_no_indice(numeros))