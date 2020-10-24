def aniversariantes_de_setembro(dicionario):

    setembro = {}
    for k,v in dicionario.items():
        if v[4] == '9':
            setembro[k]=v

    return setembro