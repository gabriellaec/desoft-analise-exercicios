def estritamente_crescente(lista):
    i = 0
    nova_lista = []
    tamanho = len(lista)
    while i < tamanho:
        if i == 0:
            nova_lista.append(lista[i])
        elif lista[i] > nova_lista[-1]:
            nova_lista.append(lista[i])
        i += 1
    return print(nova_lista)