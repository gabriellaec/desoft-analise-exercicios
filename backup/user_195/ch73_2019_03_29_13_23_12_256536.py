def remove_vogais(p):
    i=0
    S=[]
    while i<len(p):
        if p[i]!="a" and p[i]!="e" and p[i]!="i"  and p[i]!="o" and p[i]!="u":
            S.append(p[i])
        i+=1
    return S
p="arroz"
print(remove_vogais(p))
