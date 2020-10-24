def remove_vogais(palavra):
    lista = list()
    vogais = ['a', 'i', 'u', 'e', 'o']
    for e in range(len(palavra)):
        if palavra[e] not in vogais:
            lista.append(palavra[e])
    soma = ''.join(lista)
    return soma