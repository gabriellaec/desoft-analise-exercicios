def subtracao_de_listas(a,b):
    c = []
    for element in a:
        if element not in b:
            c.append(element)

    return c