def estritamente_crescente(lista):
    lis=[]
    if len(lista)>0:
        lis.append(lista[0])
    else: return lis
    i=1
    t=0
    while i < len(lista):
        if lista[i]>lis[t]:
            lis.append(lista[i])
            t+=1
            i+=1
        
    return lis
    