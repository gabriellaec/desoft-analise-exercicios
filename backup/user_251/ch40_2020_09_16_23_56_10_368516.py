lista = [0]*5
lista[0] = 1
i = 1
while i < 5:
    lista[i] = lista[i-1] + 2
    i += 1
def soma_valores(lista):
    resultado = lista[0] + lista[1] + lista[2] + lista[3] + lista[4]
    return resultado
