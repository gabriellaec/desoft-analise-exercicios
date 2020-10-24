def monta_dicionario (l1,l2):
    d={}
    i=0
    while i < len(l1):
        d[l1[i]]=l2[i]
        i+=1
    return d