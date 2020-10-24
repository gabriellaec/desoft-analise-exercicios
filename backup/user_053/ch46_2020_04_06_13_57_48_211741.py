def numero_no_indice(lista):
    nova_lista = []
    for elemento in range(0, len(lista)):
        if lista[elemento] == elemento:
            nova_lista.append(elemento)
    return nova_lista

a = [0, 10, 2, 30, 4]
print(numero_no_indice(a))