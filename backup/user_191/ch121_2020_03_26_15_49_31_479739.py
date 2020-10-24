def subtracao_de_listas:
    i=0
    o=0
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