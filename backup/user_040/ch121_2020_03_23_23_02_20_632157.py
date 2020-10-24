def subtracao_de_listas(a,b):
    x=[]
    for item in a:
        if not item in b:
            x.append(item)
    return x