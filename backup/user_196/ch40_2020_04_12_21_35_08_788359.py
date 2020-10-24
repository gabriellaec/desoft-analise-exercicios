soma = 0
def soma_valores(lista):
    lista = []
    i=0
    while i < len(lista):
        soma += lista[i]
        i+=1
        print(soma)
    return soma