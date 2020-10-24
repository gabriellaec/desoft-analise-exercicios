def separa_trios (nomes):
    trio=[]
    i=0
    while i<len(nomes):
        if i==len(nomes)-2 and (len(nomes)-2)%3==0:
            trio.append(nomes[i])
        elif i==len(nomes)-3 and (len(nomes)-3)%3==0:
            trio.append(nomes[i])
            trio.append(nomes[i+1])
        else:
            trio.append(nomes[i])
            trio.append(nomes[i+1])
            trio.append(nomes[i+2])          
        i+=3 
    return trio