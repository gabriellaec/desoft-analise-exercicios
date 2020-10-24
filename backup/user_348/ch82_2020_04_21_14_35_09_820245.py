def primeiras_ocorrencias(string):
    dicionario = {}
    for letra and i in string:
        if string[letra] != string[letra-1]:
            dicionario[letra] = i
        