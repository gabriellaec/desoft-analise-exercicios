def conta_letras(n):
    b={}
    for e in n:
        if not e in b:
            b[e]=1
        else:
            b[e]+=1
    return b
            