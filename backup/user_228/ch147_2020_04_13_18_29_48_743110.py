def mais_frequente(lista):
    dic={}
    for i in lista:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1        
    vmax=0
    for k,v in dic.items():
        if v>vmax:
            vmax=v
            palavra=k 
    return palavra 👍🏻
        



        