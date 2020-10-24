def ocorrencias_letras(stri):
    dicionario = {}
    for i in stri:
        if i not in dicionario:
            dicionario[i] = stri.count(i)

    return dicionario