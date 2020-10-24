def eh_primo(a):
    divisor = 2
    if a < 2:
        return False
    if a == 2:
        return True
    while a % divisor != 0 and divisor <= a/2:
        divisor +=1
    if a % divisor == 0:
        return False
    else:
        return True
def lista_primos(n):
    i = 2
    resultado = []
    while len(resultado) <= n-1:
        if eh_primo(i):
            resultado.append(i)
            i += 1
        else:
            i +=1
            
    return resultado