def remove_vogais(x):
    vogais = ['a','e','i','o','u']
    t = 0
    plvr = ''
    while t < len(x):
        if x[t] not in vogais:
            plvr += x[t]
        t += 1
    return plvr