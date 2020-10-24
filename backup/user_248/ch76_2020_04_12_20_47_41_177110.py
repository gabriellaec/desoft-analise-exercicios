def aniversariantes_de_setembro(dicionario):
    dicionario2={}
    for i in dicionario:
        if dicionario[i][2:4]=='09':
            dicionario2[i]=dicionario[i]
    return dicionario2