def eh_primo (numero):
	if numero == 2:
		return True
	elif numero == 0 or numero == 1:
		return False
	elif numero % 2 == 0:
		return False
	else:
		contador = 3
		while contador < numero:
			if numero % contador == 0:
				return False
			contador += 2
		return True

def maior_primo_menor_que (n):
    m = 0
    while m > n:
        if eh_primo (m):
            return True
        elif n < 0:
            print (-1)
        else:
            return False
    return m