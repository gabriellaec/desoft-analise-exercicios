def verifica_numero (n):
    if n == n[::1]**n[::1]:
        return True
    else:
        return False