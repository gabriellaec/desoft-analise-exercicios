def eh_primo(a):
    d = 2
    while d<(a-1):
        if a % d == 0:
            n = False
        d +=1
    return n
        
def maior_primo_menor_que(x):
    n = x
    while n >= 2:
        if eh_primo(n):
            return n
        n -= 1
    return -1
        
	
        