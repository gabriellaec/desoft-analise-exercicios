def verifica_numero (n):
    if n == n[::1]**n[::1]:
        return True
    elif n == 1:
        return False
    else:
        return False