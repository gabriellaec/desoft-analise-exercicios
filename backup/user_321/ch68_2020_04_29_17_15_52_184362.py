def separa_trios(l):
    s = []
    for i in range(len(l)):
        if  (i + 1) % 3 == 0:
            s.append(l[(i-2):(i+1)])
    if len(l)%3!=0:
        if len(l)%3==1 or len(l)==1:
            s.append(l[-1])
        elif len(l)%3==2 or len(l)==2:
            s.append(l[-2:])
    return s