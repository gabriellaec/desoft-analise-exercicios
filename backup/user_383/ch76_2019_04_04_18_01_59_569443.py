def aniversariante_de_setembro(dicionario):
    dic={}
    for k,v in dicionario.items():
        if dicionario[k][3:5] == '09':
            dic[k]= v
    return dic