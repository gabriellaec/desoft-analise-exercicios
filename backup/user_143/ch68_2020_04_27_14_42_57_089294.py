def separa_trios(l):
    li=[]
    p='a'
    for i in range(len(l)):
        p=l[i:i+3]
        li.append(p)
    return li