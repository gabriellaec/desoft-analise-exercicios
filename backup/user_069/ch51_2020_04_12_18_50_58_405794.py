def eh_primo (n):
    div = 3
    if n%2 == 0 and n != 2 or n == 1 or n == 0:
        return False
    
    while n > div:
        if n%div == 0:
            return False
        div += 1
    return True

def primos_entre (a,b):
    lista_primos = []
    i = a
    while i <= b:
        if eh_primo(i) == True:
            lista_primos.append(i)
        i += 1
    return lista_primos

print(primos_entre(1, 5))