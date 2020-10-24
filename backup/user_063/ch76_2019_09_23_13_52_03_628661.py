def aniversariantes_de_setembro(dicionario):
    dados_setembro = {}
    for x in dicionario:
        a = dicionario[x]
        if a[3]=='0' and a[4]=='9':
            dados_setembro[x] = a
    return dados_setembro