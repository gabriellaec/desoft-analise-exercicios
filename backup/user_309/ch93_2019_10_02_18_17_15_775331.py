def verifica_numero(n):
    while n:
        if n == n + n**n:
            return True
        elif n < 1:
            return False
        else:
            return False
            
            
            
    