def separa_trios (nomes):
    trio=[]
    i=0
    while i<len(nomes):
        if i==len(nomes)-1 and (len(nomes)-1)%3==0:
            s=nomes[i]
        elif i==len(nomes)-2 and (len(nomes)-2)%3==0:
            s=nomes[i:2]
        else:
            s=nomes[i:3]
        trio.append(s)
        i+=3 
    return trio