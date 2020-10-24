def eh_primo(a):
    divisor = 2
    if a == 1 or a <= 0:
        return False
    
    if a == 2:
        return True
    
    while a % divisor != 0 and divisor < (a-1):
        divisor += 1
    if a % divisor == 0:
        return False
    
    else:
        return True



def primos_entre(a, b):
    i = a
    resultado = []
    while i <= b:
        if eh_primo(i):
            resultado.append(i)
            i += 1
        else:
            i += 1
    return resultado
        


            