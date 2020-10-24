p = primos

def primos_entre (a, b):
	while a <= p and p <= b:
		if p == 2:
		return True
	elif p == 0 or p == 1:
		return False
	elif p % 2 == 0:
		return False
	else:
		contador = 3
        while contador < p:
			if p % contador == 0:
				return False
			contador += 2
		return True 
				print (len(p))