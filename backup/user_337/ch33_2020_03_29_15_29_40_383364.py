def eh_primo(n):
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    else:
        if n%2 == 0:
            return False
        else:
            impar = 3
            while impar < n:
                if n%impar == 0:
                    return False
                impar = impar + 2
            return True

def primos_entre(a,b):
    p = 0
    while b - a >= 0:
        while eh_primo(a) == False:
            a += 1
    p = p + 1
    a = a + 1
    return p
   
