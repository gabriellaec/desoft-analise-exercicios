def eh_primo(n):
    impar = 3
    if n <= 1:
        return False
    if n%2 == 0:
        if n == 2:
            return True
        else: 
            return False
    else:
        while impar < n:
            if n % impar == 0:
                 return False
            else:
                impar += 2
        return True
def primos_entre(a, b):
    i = 0
    p = 0
    while b < p:
        if eh_primo(i) == True:
            p += 1
        i += 1
    return p
print(primos_entre(2,3))