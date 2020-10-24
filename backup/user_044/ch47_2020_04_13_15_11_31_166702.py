def estritamente_crescente(lista):
    ls=[]
    for i in lista:
        if len(ls)!=0:
            m=max(ls)
        x=True
        while x:
            m
            if i>m:
                ls.append(i)
            else:
                x=False
    return ls           
        