def acha_bigramas(n):
    li=[]
    for i in range(len(n)-1):
        b=n[i:i+2]
        li.append(b)
    return li