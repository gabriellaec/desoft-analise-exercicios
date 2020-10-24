def remove_vogais(p):
    if p==[]:
        return p
    i=0
    lista=[]
    while i<len(p):
        if p[i]!='a' and p[i]!='e'and p[i]!='i' and p[i]!='o' and p[i]!='u':
            lista.append(p[i])
        i+=1
    return lista
            
        