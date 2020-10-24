def aniversariantes_de_setembro(x):
    dic = {}
    for e in x:
        if x[e][4] == '9':
            dic[e]=x[e]
    return dic 
                