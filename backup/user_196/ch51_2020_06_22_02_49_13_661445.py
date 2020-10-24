def eh_primo (num):
	i=2
	if num == 2:
		return True
	elif num == 0 or num == 1:
		return False
	while i < num:
		if num % i == 0:
			return False
		i = i+1
	return True

def primos_entre(a,b):
    primos = []
    for i in range (a,b+1):
        if eh_primo(i):
            primos.append(i)
    return primos  
