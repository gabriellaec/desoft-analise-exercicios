def numero_no_indice(lista):
    nova_lista = []
    i = 0
    while i < len(lista):
        if lista[i] == i:
            nova_lista.append(lista[i])
            i += 1
            
        else:
            i += 1
    return nova_lista

numeros = [0, 5, 2, 3, 5]

analise = numero_no_indice(numeros)

print (analise)