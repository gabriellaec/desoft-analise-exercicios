def subtracao_de_listas(a,b):
    for item in b:
        if item in a:
            a.remove(item)
    return a