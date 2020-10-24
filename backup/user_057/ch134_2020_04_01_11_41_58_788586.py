def verifica_quadrado_perfeito(n):
    m=n
    p=2
    while m >= 0:
        if m>0:
            m=m-p
            p=p+2
        elif m==0:
            m=m-p
    if (m**2)==n:
        return 'True'
    elif (m**2)!=n:
        return 'False'
        