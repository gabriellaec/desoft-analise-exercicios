def medias_por_inicial(n):
    s={}
    for a,b in n.items():
        z=a[0]
        s.update(z:b)
    s.update(z:b/len(z))
    return s