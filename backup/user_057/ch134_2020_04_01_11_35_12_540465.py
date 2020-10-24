def verifica_quadrado_perfeito(n):
    N=n
    m=n
    p=2
    while m >= 0:
        m=m-p
        p=p+2
    if (m**2)==N:
        return 'True'
    else:
        return 'False'
        