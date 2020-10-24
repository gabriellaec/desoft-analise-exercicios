def eh_primo(n):
    if n ==2:
        return True
    elif n > = 0:
        contador = 2
        while contador < n:
            b =  n % (contador)
            if b != 0:
                contador +=1
            else:
                return False
        return True
				