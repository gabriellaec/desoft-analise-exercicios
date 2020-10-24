def estritamente_crescente(lista):
    ls=[]
    for i in lista:
        m=max(ls)
        x=True
        while x:
            if i>m:
                ls.append(i)
            else:
                x=False
    return ls           
        