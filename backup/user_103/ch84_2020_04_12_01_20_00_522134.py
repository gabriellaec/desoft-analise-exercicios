def inverte_dicionario(dicionario):
    dic_inverte={}
    for i in dicionario:
        dic_inverte[dicionario.values]=dicionario.keys
    return dic_inverte
        