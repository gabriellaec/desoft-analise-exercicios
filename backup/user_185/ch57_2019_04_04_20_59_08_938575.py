def soma_impares(lista):
    contador = 0
    soma = 0
    while contador < len(lista):
        if lista[contador]%2 == 1:
            soma = soma + lista[contador]
        contador = contador + 1
    return soma

    