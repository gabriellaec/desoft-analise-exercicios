def subtracoo_de_listas(a,b):
    x=[]
    for e in a:
        if not e in b:
            x.append(e)
    return x