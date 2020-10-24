def separa_trios(l):
    li=[]
    p='a'
    i=0
    while i<len(l):
        p=l[i:i+3]
        li.append(p)
        i+=3
    return li