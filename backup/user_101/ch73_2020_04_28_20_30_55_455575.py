def remove_vogais(s):
    v = ['a','e','i','o','u']
    f = ''
    for e in s:
        if e not in v:
            f += e
    return f