numeros = [2, 5, 89, 413, 3, 10, 96, 77, 57, 197, 32]

def soma_impares(lista):
    i = 0
    soma_impar = 0
    while i < len(lista):
        if lista[i] %2 == 0:
            i += 1
        else:
            soma_impar += lista[i]
            i += 1
    return soma_impar

soma = soma_impares(numeros)
print(soma)