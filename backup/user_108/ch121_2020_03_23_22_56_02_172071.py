def subtracao_de_listas(a,b):
    c = []
    for item in a:
        if not item in b:
            c.append(item)
    return c
