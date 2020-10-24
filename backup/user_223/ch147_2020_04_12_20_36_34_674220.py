def mais_frequente(l1):
    dic={}
    for e in l1:
        if e in dic:
            dic[e]+=1
        else:
            dic[e]=1
      
    palavra = [0]
    for i in dic.items():
        if dic.values(i+1) > dic.values(i):
            del palavra [0]
            palavra.append(dic.keys(i+1))
            return palavra