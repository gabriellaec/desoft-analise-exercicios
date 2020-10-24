def separa_trios(l):
    li=[]
    lis=[]
    p='a'
    for i in range(len(l)):
        p=l[i:i+3]
        li.append(p)
    if len(l)%3==1:
        lis=[l[len(l)-1]]
        li=li+lis
    elif len(l)%3==2:
        lis=[l[len(l)-2], l[len(l)-1]]
        li=li+lis
    return li