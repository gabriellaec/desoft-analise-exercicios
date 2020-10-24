
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

def primos_entre(a,b):
    m=a
    primos = []
    while m<=b:
        if eh_primo(m)==True:
            primos.append(m)
        m=m+1
        p = len(primos)

    return p