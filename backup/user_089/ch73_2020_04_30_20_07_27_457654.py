def remove_vogais(x):
    z = ['a','e','i','o','u']
    s = ''
    for e in x:
        if e not in z:
            s += e
    return s