def quantos_uns(numero):
    n=0
    i=0
    listanova=[]
    for i in numero:
        listanova.append(i)
    for i in listanova:
        if i=="1":
            n+=1
    return n
            