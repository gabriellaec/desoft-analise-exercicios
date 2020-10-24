def quantos_uns(num):
    nome=str(num)
    e=0
    c=0
    while e<len(nome):
        if nome[e]==1:
            c+=1
        e+=1
    return c