def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    for i in range(3, n, 2):
        if n%2==0:
            return False
        elif n%i==0:
            return False
    else:
        return True
    
def  maior_primo_menor_que(n):
    p = -1
    while n>0:
        if n ==2:
            return 2
        else:
            if eh_primo(n):
                p == n
            elif:
                n-=1
    return p
    
    
    
    