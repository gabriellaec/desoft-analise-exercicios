def eh_primo(n):
    if n <= 1:
        return False
    resultado = True
    for i in range(2,n-1):
        if n % i == 0:
            resultado = False
    return resultado