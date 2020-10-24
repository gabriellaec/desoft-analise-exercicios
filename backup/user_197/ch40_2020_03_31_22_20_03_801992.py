lista=[2,3,4,5]
def soma_valores(lista):
    i=0
    soma=0
    while i<len(lista):
        soma=soma+lista[i]
        i+=1
    return soma

print(soma_valores(lista))
