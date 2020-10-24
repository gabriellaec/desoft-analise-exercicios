def aniversariantes_de_setembro(dicionario):
    dic={}
    for nome, data in dicionario.items():
        if data[3]=='0' and data[4]=='9':
            dic[nome]=data
    return dic
        