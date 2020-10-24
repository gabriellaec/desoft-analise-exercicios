def acha_bigramas(n):
    li=[]
    for i in range(1,len(n),2):
        b=n[i:i+1]
        li.append(b)
    return li