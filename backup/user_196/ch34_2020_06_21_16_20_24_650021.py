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

def maior_primo_menor_que(n):
    for c in range(n, 0, -1):
        if eh_primo(c):
            return c
    return -1