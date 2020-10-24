def agrupa_por_idade(d1):
    d={}
    l=[]
    ln=[]
    for j,i in d1.items():
        l.append(i)
        ln.append(j)
    i=0
    lisc=[]
    lisa=[]
    lisadu=[]
    lisi=[]
    while i<len(l):
        if l[i]<=11:
            lisc.append(ln[i])
        elif l[i]>11 and l[i]<=17:
            lisa.append(ln[i])
        elif l[i]>17 and l[i]<=59:
            lisadu.append(ln[i])
        else:
            lisi.append(ln[i])
        i+=1
    d['criança']=lisc
    d['adolescente']=lisa
    d['adulto']=lisadu
    d['idoso']=lisi
    return d
            
    