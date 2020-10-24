def subtracao_de_listas(x,y):
    for item in y:
        if item in x:
            x.remove(item)
    return x