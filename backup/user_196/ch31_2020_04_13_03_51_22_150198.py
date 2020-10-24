def maior_primo_menor_que(n):
	if n == 2:
		return 2
	elif n == 0 or n == 1:
		return -1
    i=2
	while n<=num:
		if num % i == 0:
			return num
		i = i+1
	return True