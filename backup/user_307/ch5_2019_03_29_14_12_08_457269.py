def verifica_primo(n):
	primo=True
	i=2
	while i<n:
		if n%i==0:
			primo=False
		i+=1
	return primo
		

def maior_primo_menor_que(n):
	i=n
	while i>1:
		if verifica_primo(i):
            return i
        i-=1
    return -1