def estritamente_crescente(lista):
    ls=[]
    m=0
    for i in lista:
        if len(ls)!=0:
            m=max(ls)
        if i>m:
            ls.append(i)
    return ls           
        