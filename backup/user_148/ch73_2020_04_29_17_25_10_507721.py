def remove_vogais(str):
    lista = []
    i = 0
    while i<len(str):
        if str[i] != 'a', 'e', 'i', 'o', 'u':
            lista.append(str[i])
        i += 1
    return lista
