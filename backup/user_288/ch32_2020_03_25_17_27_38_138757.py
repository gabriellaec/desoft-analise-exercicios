n = 0
lista = []
def lista_primos (lista, n):
	while n < len(lista):
		if n == 2:
		return True
	elif n == 0 or n == 1:
		return False
	elif n % 2 == 0:
		return False
	else:
		contador = 3
		while contador < n:
			if n % contador == 0:
				return False
				contador += 2
		return True 
				print (lista[n])
    