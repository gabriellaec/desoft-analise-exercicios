def quantos_uns(n):
    nlist = list(str(n))
    dic={}
    for e in nlist:
        if e in dic:
            dic[e]+=1
        else:
            dic[e]=1
    numero_1=0
    for k in dic.keys():
        if k=="1":
            numero_1 = dic[k]
            return numero_1