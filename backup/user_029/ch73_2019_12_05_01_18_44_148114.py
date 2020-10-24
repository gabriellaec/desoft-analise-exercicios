def remove_vogais(x):
    vogais = ['a','e','i','o','u']
    x1 = x.replace('a','')
    lista = []
    for i in x:
        if i in vogais:
            x.del(i)
    return x1