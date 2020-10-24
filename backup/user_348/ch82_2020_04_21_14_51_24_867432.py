def primeiras_ocorrencias(string):
    dicionario = {}
    for letra in string:
        if string[letra] not in dicionario:
            dicionario[letra] = letra
        return dicionario
       
        