def soma_de_lista():
    lista = []
    length = 0
    soma = 0
    n = 1
    lista[0] = int(input("numero "))
    
    while (lista [n] != 0 and lista[0] != 0):
        lista[n] = int(input("numero "))
        n += 1
        
    while (length < len(lista)):
        soma += lista[n]
        n += 1
    return (soma)
print(soma_de_lista())