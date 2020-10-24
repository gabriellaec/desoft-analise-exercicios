def eh_primo(a):
    n = True
    d = 2
    while d<a:
        if a % d == 0:
            n = False
        d +=1
    return n
        
def maior_primo_menor_que(x):
    n = x
    while n >= 2:
        if eh_primo(n):
    	return n
	if x <= 0:
        return '-1'
        
	
        