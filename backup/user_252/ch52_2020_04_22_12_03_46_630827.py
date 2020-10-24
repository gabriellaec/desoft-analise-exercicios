def calcula_total_da_nota(l1, l2):
    a=len(l1)
    b=len(l2)
    x=0
    y=0
    s=0
    while x<a and y<b:
        s+=(l1[x]*l2[y])
        x+=1
        y+=1
    return s