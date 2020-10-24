def estritamente_crescente(lista):
    i = 0
    nova_lista = []
    while i <= len(lista):
        for num in lista:
            if (i != 0) and (lista[i] > nova_lista[-1]):
                nova_lista.append(num)

    print(nova_lista)