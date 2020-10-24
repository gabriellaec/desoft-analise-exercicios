def eh_primo(n):
    k = 0
    if n < 2 :
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i != 0:
                k += 1
        if k == (n-2) :
            return True
        else:
            return False
        
def verifica_primos(d):
    new_d = {}
    for n in d:
        new_d[n] = eh_primo(n)
    return new_d
        