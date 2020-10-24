def subtracao_de_listas(a,b):
    i=0
    o=0
    if a==[]:
        return(a)
    elif b==[]:
        return(a)
    elif (a==[] and b==[]):
        return(a)
    else:
        while o<len(b):
            while i<len(a):
                if a[i]==b[o]:
                    del a[i]
                    i+=1
                else:
                    i+=1
            i=0
            o=o+1
    return(a)