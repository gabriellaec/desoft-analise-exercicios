
def verifica_numero(n):
    soma = 0
    if n < 1:
        return False
    else:
        for i in range(n):
            soma += i**i
        if soma == n:
            return True
        else: 
            return False
    return True