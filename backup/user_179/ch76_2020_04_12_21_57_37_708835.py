def aniversariantes_de_setembro (dicionario):
    i = 0
    while i < len(dicionario):
        data = dicionario.get(i)
        if data[4] == '0' and data[5] == '9':
            lista.append(dicionario(i))
            i = i + 1
        else:
            i = i + 1
    return lista