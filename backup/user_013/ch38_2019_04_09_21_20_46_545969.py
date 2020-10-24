def eh_primo(n):
    resultado = True
    for i in range(2,n-1):
        if n % i == 0:
            resultado = False
    return resultado

def primos_entre(a,b):
    A = []
    for i in range(a,b+1):
        if eh_primo(i) == True:
            A.append(i)
    return A