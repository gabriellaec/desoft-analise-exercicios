def soma_valores(lista):
    contador = 0
    soma = 0

    while contador < len(lista):
        soma += lista[contador]
        contador += 1
    
    return soma