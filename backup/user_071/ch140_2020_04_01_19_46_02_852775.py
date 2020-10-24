def notas(l1):
    i=0
    c1=0
    c2=0
    c3=0
    l2=[]
    while i<len(l1):
        if 0<=l1[i]<5:
            c1+=1
        elif 5<=l1[i]<=7:
            c2+=1
        elif l1>7:
            c3+=1
        i+=1
    l2.append(c1, c2, c3)
    return l2