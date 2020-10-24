def monta_dicionario(x,y):
    d={}
    for e in x:
        d= e.key()
    for e in y:
        d=e.values()
    return d
    