def eh_primo (n):
    if n == 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    else:
        i=3
        primu=True
        while i<n and primu:
            if n%2==0:
                primu = False
                return False
            elif n%i!=0:
                i=i+2
            elif n%i==0:
                primu = False
                return False
        if i>=n:
            return True

def primos_entre (a,b):
    n = 0
    lista = []
    while n <= b:
        if eh_primo(n) and n >= a:
            lista.append(n)
        n+=1
    return lista           