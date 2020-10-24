def quantos_uns(n):
    nlist = list(str(n))
    dic={}
    for e in nlist:
        if e in dic:
            dic[e]+=1
        else:
            dic[e]=1
    for k in dic.keys():
        if k=="1":
            print(dic[k])