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
    

def lista_primos (n):
    lista = []
    i = 0
    while len(lista) < n:
        if eh_primo (i):
            lista.append (i)
        i += 1
    return lista
        