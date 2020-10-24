def eh_primo (m):
    if m == 0:
        return False
    elif m == 1:
        return False
    elif m == 2:
        return True
    elif m == 3:
        return True
    else:
        i=3
        primu=True
        while i<m and primu:
            if m%2==0:
                primu = False
                return False
            elif m%i!=0:
                i=i+2
            elif m%i==0:
                primu = False
                return False
        if i>=m:
            return True

def maior_primo_menor_que(n):
    primomax = -1
    m=0
    while m<=n:
        t=eh_primo(m)
        if t:
            primomax = m
        m = m + 1
     
    return primomax