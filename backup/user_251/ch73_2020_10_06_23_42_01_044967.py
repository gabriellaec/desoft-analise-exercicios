def remove_vogais(a):
    i = 0
    resultado = []
    vogais = ['a', 'e', 'i', 'o', 'u']
    while i < len(a):
        if a[i] not in vogais:
            resultado.append(a[i])
            i += 1
        else:
            i += 1
    return resultado