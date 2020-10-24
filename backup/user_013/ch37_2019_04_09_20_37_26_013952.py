def eh_primo(n):
    resultado = True
    for i in range(2,n-1):
        if n % i == 0:
            resultado = False
    return resultado

def lista_primos(n):
    A = [0]*n
    i = 2 
    k = 0 
    while k < n:
        if eh_primo(i):
            A[k] = i
            k += 1
        i += 1
    return A