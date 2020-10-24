def lista_caracteres(x):
    i=0
    s=[]
    k=0
    while i<len(x):
        s.append (x[i])
        i+=1
    l=len(s)
    while k<len(s):
        if s[k]==s[(l-1)]:
            del s[k]
        k+=1
        l-=1
    return s