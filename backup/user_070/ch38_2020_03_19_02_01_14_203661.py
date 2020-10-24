def quantos_uns(n):
    a = 0
    i = 1
    while n>=i:
        if n%i>=i/10 and n%i<2*i/10:
            a += 1
            i = i*10
        else:
            i = i*10
    i = i/10
    if n/i>=1 and n/i<2:
        a +=1
        return a
    else:
        return a