def eh_primo(n):
    d = 2
    while d<n:
        if n % d == 0:
            return False
        else:
            d += 1
    return True  

def num_primo_mais_prox(a):
    if a > 1:
        while not eh_primo(a):
            a -= 1    
        return a
    else:
        return -1