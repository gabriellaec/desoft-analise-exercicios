def eh_primo (n):
    if n ==2:
        return True
    elif n % 2 == 0:
        return False
    elif n % 2 != 0:
        contador = 2
        while n % (n-contador) == 0:
            return false
            contador = contador + 2
	else:
        return True
        