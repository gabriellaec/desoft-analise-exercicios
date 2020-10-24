def aniversariantes_de_setembro(dicionario):
    dic = {}
    for k, v in dicionario.items():
        if v[4] == '9':
            dic[k] = v
    
    return dic
