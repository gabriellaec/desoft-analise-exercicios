def quantos_uns(n):
    uns=0
    n=str(n)
    tamanho=len(n)
    i=0
    while i<tamanho:
        if n[i]=="1":
            uns+=1
        i+=1
    return uns
