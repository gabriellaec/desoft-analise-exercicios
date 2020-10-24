lista = [1,2,3,4,5,6,7,8,9]
num_elementos = len(lista)
x = 0
soma = 0

def soma_valores(x):
    while x < num_elementos:
        soma = soma + lista[x]
        x = x + 1
    return soma