def remove_vogais(palavra):
    vogais = ['a', 'i', 'u', 'e', 'o']
    for e in range(len(palavra)):
        if palavra[e] in vogais:
            del palavra[e]
    return palavra