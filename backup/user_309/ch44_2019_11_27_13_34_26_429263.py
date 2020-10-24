lista = [0,1,2,3,4,5,6,7,8,9,10]

def soma_valores(lista):
    i=0
    soma=0
    while i < len(lista):
        soma+=lista[i]
       	i+=1
    return soma

print(soma_valores(lista))