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
    while a<=b:
        while eh_primo(a) == False:
            a += 1
        p += 1
        a += 1
    return p