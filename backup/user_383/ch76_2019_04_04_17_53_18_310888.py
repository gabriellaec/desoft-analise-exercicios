def aniversariantes_de_setembro(dicionario):
    dic={}
    for k,v in dicionario.items():
        if dicionario[k][3:5] == '09':
            dic[v]='09'
    return k,v