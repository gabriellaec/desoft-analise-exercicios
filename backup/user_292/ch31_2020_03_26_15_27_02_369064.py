def eh_primo(n):
	if n<2:
		return False
	elif n==2:
		return True
	elif n%2==0:
		return False
	else:
		i=3
		while (n%i!=0):
			i=i+2
		if n==i:
			return True
	return False 
    