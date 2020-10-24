def separa_trios(l):
    s='a'
    k='c'
    p='b'
    li=[]
    for i in l:
        if len(l)%3==0:
            p=l[::3]
        elif len(l)%3==1:
            p=l[::3]
            p.append(len(l)-1)
        else:
            p=l[::3]
            s=l[len(l)-2]
            k=l[len(l)-1]
            li.append(s)
            li.append(k)
            p+=li
    return p
            p.append