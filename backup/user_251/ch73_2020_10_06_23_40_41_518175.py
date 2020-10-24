def remove_vogais(a):
    i = 0
    resultado = a
    vogais = ['a', 'e', 'i', 'o', 'u']
    while i < len(a):
        if a[i] in vogais:
            del a[i]
            i += 1
        else:
            i += 1
    return resultado