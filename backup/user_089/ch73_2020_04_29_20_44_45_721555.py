def remove_vogais(x):
    z = ['a','e','i','o','u']
    for e in x:
        if e in z:
            x = x - e
    return x