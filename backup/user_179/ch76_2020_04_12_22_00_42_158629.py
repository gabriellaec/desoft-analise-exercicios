def aniversariantes_de_setembro (dicionario):
    i = 0
    while i < len(dicionario):
        data = dicionario.get(i)
        if data[3] == '0' and data[4] == '9':
            lista.append(dicionario(i))
            i = i + 1
        else:
            i = i + 1
    return lista