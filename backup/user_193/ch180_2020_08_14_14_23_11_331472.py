def ocorrencias_letras(s):
    d=[]
    v=[]
    for i in s:
        d.append(i)    
    k=list(set(d))
    for z in range(len(k)):
        v.append(0)
    for y in d:
        ri=k.index(y)
        v[ri]+=1
    res={k[i]: v[i] for i in range(len(k))}
    return res