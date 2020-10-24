def remove_vogais(string):
    lista = []
    for elemento in string:
        lista.append(elemento)
    e = 0
    while e < len(lista):
        if lista[e] == 'a' or lista[e] =='e' or lista[e] =='i' or lista[e] =='o' or lista[e] =='u':
            del lista[e]
        else:
            e += 1
    return ''.join(lista)