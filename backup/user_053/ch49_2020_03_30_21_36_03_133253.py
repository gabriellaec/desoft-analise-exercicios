def inverte_lista(lista):
    nova_lista = [0]*len(lista)
    i = 0
    while i < len(lista):
        nova_lista[i] = lista[len(lista) - i - 1]
        i += 1
    return nova_lista

teste = [1, 2, 3, 4, 5]
print(inverte_lista(teste))