def subtracao_de_listas(x,y):
    for palavra in y:
        if palavra in x:
            x.remove(palavra)
    return x