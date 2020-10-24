def aniversariantes_de_setembro(dic):
    novo_dic={}
    lis=[]
    lisnomes=[]
    for k,v in dic.items.():
        lisnomes.append(k)
        lis.append(v)
    i=0
    while i<len(lis):
        if lis[i][3:5] == '09':
            novo_dic[lisnomes[i]]=lis[i]
        i+=1
    return novo_dic