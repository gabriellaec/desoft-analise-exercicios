def classifica_lista(l):
    i=1
    t=[]
    while i<len(l):
        if l[i]>l[i-1]:
            t.append(1)
        elif l[i]>l[i-1]:
            t.append(-1)
        i +=1
    med= sum(t)/len(t)
    if med== (1) and len(t)>0:
        return "crescente"
    elif med== (-1) and len(t)>0:
        return "decrescente"
    elif -1<med<1 :
        return "nenhum"
    elif len(t)<=0:
        return "nenhum"