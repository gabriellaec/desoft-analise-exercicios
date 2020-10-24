def apaga_repetidos(x):
    nova = ''
    for e in x:
        if e in nova:
            nova = nova +"*"
        else:
            nova = nova+ e 
    return nova