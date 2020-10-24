def lista_caracteres(s):
    lista = []
    for i in range(len(s)):
        if s[i] not in lista:
            lista.append(s[i])
    return lista