def separa_trios(n):
    l=[]
    i=0
    t=0
    while i<len(n):
        while t<3:
        l[t].append(n[i])
        i+=1
    t=t-2
    