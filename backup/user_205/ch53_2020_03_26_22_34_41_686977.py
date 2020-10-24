soma = 0
def soma_impares(lista):
    for i in range(len(lista)):
        if lista[i]%2!=0:
            soma+=lista[i]
    		return soma