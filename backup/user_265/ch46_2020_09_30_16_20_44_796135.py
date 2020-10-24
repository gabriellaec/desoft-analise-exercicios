def numero_no_indice(a):
    lista = []
    nova = []
    i = 0
    a = 0
    while a < len(lista):
        if lista[i] == i:
            nova.append(i)
            a += 1
    return nova
