def remove_vogais(x):
    alfabeto = ['a','e','i','o','u']
    t = 0
    plvr = ['']
    while t < len(x):
        if x[t] not in alfabeto:
            plvr = x[t]
            t += 1
            break
        t += 1
    while t < len(x):
        if x[t] not in alfabeto:
            plvr += x[t]
        t += 1
    return plvr