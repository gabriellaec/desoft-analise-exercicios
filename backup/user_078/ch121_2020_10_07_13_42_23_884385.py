
def subtracao_de_listas(lista1, lista2):

    nova_lista =[]

    for elemento in lista1:

        if elemento not in lista2:
            nova_lista.append(elemento)

    return nova_lista