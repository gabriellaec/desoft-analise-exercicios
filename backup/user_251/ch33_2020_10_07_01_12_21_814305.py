def eh_primo(c):
    divisor = 2
    if c == 1 or c == 0:
        return False
    
    if c == 2:
        return True
    
    while c % divisor != 0 and divisor < (c-1):
        divisor += 1
    if c % divisor == 0:
        return False
    
    else:
        return True

def primos_entre(b, c):
    numero_de_primos = 0
    contador = 0
    while contador < b:
        contador += 1
    while b <= contador and contador <=c:
        if eh_primo(contador):
            numero_de_primos += 1
            contador += 1
        else:
            contador += 1
    return numero_de_primos
print(primos_entre(a,b))