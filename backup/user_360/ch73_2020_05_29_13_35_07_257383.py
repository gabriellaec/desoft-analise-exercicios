def remove_vogais(x):
    vogais = ['a', 'e', 'i', 'o', 'u']
    lista = list()
    for i in x:
        lista.append(i)
        for t in vogais:
            if i == t:
                lista.remove(i)
    return ("".join(lista))