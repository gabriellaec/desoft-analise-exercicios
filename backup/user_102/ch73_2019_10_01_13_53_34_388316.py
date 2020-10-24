def remove_vogais(x):
    a = True
    while a:
        x.replace('a','')
        x.replace('e','')
        x.replace('i','')
        x.replace('u','')
        x.replace('o','')
        a = False
    return x