
def eh_primo(n):
    if n < 2:
        return False
    else:
    	conta = 2
    	while conta < n:
            if n % 2 == 0 or n % conta == 0:
                return False
            conta += 1
    	return True
def imprime_primos(n):
    i = 0
    while i <= n:
        if eh_primo(i) == True:
            print(i)
        i += 1
        i += 1