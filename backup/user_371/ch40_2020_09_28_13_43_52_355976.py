lista = []
soma = 0
i=len(lista)
j=0
def soma_valores(lista):
    while j<i:
        soma = lista[j]+soma
        j+=1
    return soma