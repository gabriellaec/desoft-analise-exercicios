def medias_por_inicial(n):
    b={}
    s={}
    for a,j in n.items():
        z=a[0]
        s[z]=[]
    for e in n:
        if not e in b:
            b[e]=1
        else:
            b[e]+=1
    for c,d in n.items():
        y=c[0]
        s[y].append(d)
    for e,f in n.items():
        v=e[0]
    s.update({v:f/len(s)})
    return s
print(medias_por_inicial({'Andrew Ayres': 6, 'FÃ¡bio Ikeda': 10, 'FÃ¡bio Kurauchi': 9, 'Raul Hage': 8}))