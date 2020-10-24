def acha_bigramas(n):
    li=[]
    b=n[0:2]
    li.append(b)
    for i in range(len(n)-1):
        c=n[i:i+2]
        if c!=b:
            b=c
            li.append(b)
    return li