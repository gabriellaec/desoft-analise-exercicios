def estritamente_crescente(lista):
    i = 0
    nova_lista = []
    nova_lista.append(lista[0])
    while lista[i+1] > lista[i]:
        nova_lista.append(lista[i+1])
        i += 1
    return nova_lista

a = [10, 15, 11, 12, 13, 14]
b = estritamente_crescente(a)

print(b)