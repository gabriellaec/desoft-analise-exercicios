lista=[1,2,3,4,5,6,7]
def soma_impares(lista):
    soma=0
    i=0
    foi i in range(len(lista)):
        soma=lista[i]+soma
        i+=2
    return soma
    