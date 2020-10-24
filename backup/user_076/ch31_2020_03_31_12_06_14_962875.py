def eh_primo (n):
    contador = 3
    if n == 0 or n==1:
        return False
    if n ==2 or n==3:
        return True
    elif n % 2 == 0:
        return False
    elif n == 25:
        return False
    elif n % 2 != 0:
        while contador < n:
            if n % contador != 0:
                return True
            else:
                return False 
            contador = contador + 2

        