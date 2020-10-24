def eh_primo(p):
    if p <= 1:
        return False
    
    np = 3
    while np < p:
        
        if p%2 == 0 or p%np == 0:
            return False
        np +=2
    return True 

def maior_primo_menor_que(n):
    while eh_primo(n) == False:
        if n<2:
            return -1
        else:
            n-=1
    else:
        return n
    