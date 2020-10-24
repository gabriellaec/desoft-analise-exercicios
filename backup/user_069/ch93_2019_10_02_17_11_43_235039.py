def verifica_numero (n):
    if n == n[::1]**2n[::1]:
        return True
    else:
        return False