def quantos_uns(nome):
    n=str(nome)
    e=0
    c=0
    while e<len(n):
        if n[e]==1:
            c+=1
        e+=1
    return c