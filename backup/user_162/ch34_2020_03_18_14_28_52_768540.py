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
    j = n-1
    while eh_primo(j) == False:
        if n<3:
            return -1
        else:
            j-=1
    else:
        return j