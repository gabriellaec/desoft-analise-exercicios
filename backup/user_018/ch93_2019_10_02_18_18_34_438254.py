soma = 0
def verifica_numero(n):
    if n < 1:
        return False
    for i in range(n):
        soma += i**i
    if soma == n:
        return True
    else: 
        return False
    return True