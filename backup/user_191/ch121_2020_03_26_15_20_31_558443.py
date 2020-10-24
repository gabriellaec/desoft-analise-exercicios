def subtracao_de_listas(a,b):
    i=0
    o=0
    n=[]
    if (len(a)>0 and len(b)>0):
        while i<len(a):
            if a[i]==b[o]:
                i+=1
            else:
                n.append(a[i])
                i+=1
        i=0
        while o<len(b):
            if a[i]==b[o]:
                o+=1
            else:
                n.append(a[i])
                o+=1
        return(n)
    elif len(a)>0:
        while i<len(a):
            if a[i]==b[o]:
                i+=1
            else:
                n.append(a[i])
                i+=1
    elif len(b)>0:
        while o<len(b):
            if a[i]==b[o]:
                o+=1
            else:
                n.append(a[i]) 
                o+=1
    else:
        break
            