def primeiras_ocorrencias(palavra):
    dicionario={}
    ocorrencia=0
    for letra in palavra:
        if not letra in dicionario:
            dicionario[letra]=ocorrencia
        ocorrencia+=1
    return dicionario