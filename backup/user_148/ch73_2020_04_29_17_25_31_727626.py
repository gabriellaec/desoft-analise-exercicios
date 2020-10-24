def remove_vogais(str):
    lista = []
    i = 0
    while i<len(str):
        if str[i] != 'a' or 'e' or 'i' or 'o' or 'u':
            lista.append(str[i])
        i += 1
    return lista
