def subtracao_de_listas(a,b):
    #return (filter(lambda item: not item in b,a))
    for item in b:
        if item in a:
            a.remove(item)
    return a
