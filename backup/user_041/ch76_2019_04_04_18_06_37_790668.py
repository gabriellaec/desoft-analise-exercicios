def aniversariantes_de_setembro(dicionario):
    dic={}
    for pessoa,aniversario in dicionario.items():
        if aniversario[3:5]=='09':
            dic[pessoa]=aniversario
    return dic