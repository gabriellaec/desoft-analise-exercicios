def quantos_uns(n):
    s=0
    i=0
    while i<len(n):
        if n[i]=='1':
            i+=1
            s+=1
        else:
            i+=1
    return s
     