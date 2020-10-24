def remove_vogais(str):
    lista = []
    i = 0
    while i<len(str):
        if str[i] != 'a' and 'e' and 'i' and 'o' and 'u':
            lista.append(str[i])
        i += 1
    return lista
