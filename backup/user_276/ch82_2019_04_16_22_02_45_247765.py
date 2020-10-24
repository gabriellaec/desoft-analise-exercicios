dicionario = {}
def primeiras_ocorrencias(string):
    while i < len(string):
        if string[i] in dicionario:
            dicionario[string[i]] = i
        i += 1
        return dicionario
         