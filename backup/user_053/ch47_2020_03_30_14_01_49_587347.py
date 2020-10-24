def estritamente_crescente(lista):
    i = 0
    nova_lista = []
    nova_lista.append(lista[0])
    while i < (len(lista) - 1):
        if lista[i+1] > lista[i]:
            nova_lista.append(lista[i+1])
            i += 1
        else:
            i += 1
    return nova_lista

a = [1, 1, 2, 2, 3, 3]
b = estritamente_crescente(a)

print(b)