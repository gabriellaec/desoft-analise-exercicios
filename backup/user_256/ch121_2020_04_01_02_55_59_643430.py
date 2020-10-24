def subtracao_de_listas( lista1, lista2):
    nova = []
    for elem in lista1:
        if not elem in lista2:
            nova.append(elem)
            return nova