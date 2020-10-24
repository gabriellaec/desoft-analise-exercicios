def eh_crescente(lista):
    i=0
    maior=lista[0]
    while i < len(lista):
        if lista[i] > maior:
            maior=lista[i]
            resposta='True'
        else:
            resposta='False'
        i+=1	
    return resposta
l=[1, 2, 3, 4]
l2=[1,5,2,3]
print(eh_crescente(l))
print(eh_crescente(l2))