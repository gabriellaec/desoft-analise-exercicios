def subtracao_de_listas( lista1, lista2):
    nova = []
    for objeto in lista1 and not objeto in lista2:
        nova.append(objeto)
        return objeto