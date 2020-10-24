def medias_por_inicial (d1):
    l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    d={}
    m=0
    e=0
    d=0
    for j,i in d1.items():
        c=0
        while c<len(l):
            if j[0]==l[c]:
                d+=1
                e+=i
                m=e/d
                c=len(l)
        d[l[c]]=m
            
            