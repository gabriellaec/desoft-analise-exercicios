def calcula_total_da_nota(l1, l2):
    a=len(l1)
    b=len(l2)
    i=0
    j=0
    s=0
    while i<a and j<b:
        s+=(l1[i]*l2[j])
        i+=1
        j+=1
    return s