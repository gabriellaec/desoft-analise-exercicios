def separa_trios(l):
    p='b'
    li=[]
    for i in range(len(l)):
        if len(l)%3==0:
            p=l[::3]
        elif len(l)%3==1:
            p=l[::3]
            p.append(len(l)-1)
        else:
            p=l[::3]
            li=[l[len(l)-2], l[len(l)-1]]
            p=p+li
    return p