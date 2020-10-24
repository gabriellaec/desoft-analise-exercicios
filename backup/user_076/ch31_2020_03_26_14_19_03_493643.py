def eh_primo (n):
    contador = 2
    if n ==2:
        return True
    elif n % 2 == 0:
        return False
    elif n % 2 != 0:
        while n % (n-contador) == 0:
            contador = contador + 2
        return False
    else:
        return True      

        