def aniversariantes_de_setembro(aniversario):
    dic={}
    for k,v in aniversario.items():
        if aniversario[k][3:5]=='09':
            dic[k]=v
    return dic