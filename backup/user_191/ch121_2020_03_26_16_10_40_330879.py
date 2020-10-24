def subtracao_de_listas(a,b):
    i=0
    o=0
    t1=len(a)
    t2=len(b)
    while o<t2:
        while i<t1:
            if a[i]==b[o]:
                del a[i]
                i+=1
            else:
                i+=1
        i=0
        o=o+1
        return(a)