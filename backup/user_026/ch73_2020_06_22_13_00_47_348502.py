def remove_vogais(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    lista = []
    for i in palavra:
        lista.append(i)
        for p in vogais:
            if i == p:
                lista.remove(i)
    return (''.join(lista))