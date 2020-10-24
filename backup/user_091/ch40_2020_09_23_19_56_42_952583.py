lista=[]
def soma_valores(lista):
    i=0
    soma=0
    while(i<len(lista)):
        soma += lista[i]+lista[i+1]+lista[i+2]
        i+=1

        return soma

