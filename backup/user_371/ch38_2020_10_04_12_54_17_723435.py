def quantos_uns(n):
    j=0
    numero_uns=0
    n=str(n)
    while len(n)>j:
        if n[j]=="1":
            numero_uns+=1
            j+=1
        else:
            j+=1
    return numero_uns