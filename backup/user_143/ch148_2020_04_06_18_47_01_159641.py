def conta_letras(s):
    di={}
    l=[]
    for i in range(len(s)):
        z=s[i]
        l.append(z)
    a=0
    while a<len(l):
        b=0
        c=0
        while b<len(l):
            if l[a]==l[b]:
                c+=1
                b+=1
            else:
                b+=1
        di[l[a]]=c
        a+=1
    return di
            