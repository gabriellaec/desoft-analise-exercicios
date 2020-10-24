def subtracap_de_listas(a,b):
    i=0
    o=0
    n=[]
    while i<len(a):
        if a[i]==b[o]:
            i+=1
        else:
            n.append(a[i])
    i=0
    while o<len(b):
        if a[i]==b[o]:
            i+=1
        else:
            n.append(a[i])
    return(n)
            
            