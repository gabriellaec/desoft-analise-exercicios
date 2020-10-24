def aniversariantes_de_setembro(dic):
    novodic={}
    lis = []
    lisnomes=[]
    for k, v in dic.items():
        lisnomes.append(k)
        lis.append(v)
    i = 0
    while i < len(lis):
        if lis[i][3:5] == '09':
            novodic[lisnomes[i]] = lis[i]
        i+=1
    return novodic
        