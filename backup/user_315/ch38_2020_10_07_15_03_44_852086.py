def quantos_uns(x):
    i = 0
    j = 1
    while x >= i:
        if x%j>=j/10 and n%j<2*j/10:
            i+=1
            j*=10
        else:
            j*=10
    j=j/10
    if x/j>=1 and x/j<2:
        i+=1
        return i
    else:
        return i        