def verifica_numero(n):
    while n > 1:
        return True
    if n == n**n:
        return True
    else:
        return False