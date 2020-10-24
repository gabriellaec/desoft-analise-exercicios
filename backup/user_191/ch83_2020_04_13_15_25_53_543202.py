def medias_por_inicial(n):
    qnt={}
    nota={}
    for a in n:
        if a[0] not in qnt:
            qnt[a[0]]=qnt[a]
            nota[a[0]]=1
        else:
            qnt[a[0]]+=qnt[a]
            nota[a[0]]+=1
    for i,o in qnt.items():
        qnt[i]=o/nota[i]
    return qnt