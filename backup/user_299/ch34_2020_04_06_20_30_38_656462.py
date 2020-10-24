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
    m=0
    while m<=n:
        if eh_primo(m) == True:
            n = m
        else:
            n = -1
        m = m + 1      
    return n