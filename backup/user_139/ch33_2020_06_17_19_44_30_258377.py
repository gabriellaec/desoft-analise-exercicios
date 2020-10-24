def eh_primo (n):
    if n == 2:
        return True
    elif n == 0 or n == 1 or n %2 == 0:
        return False
    i = 3
    while i < n:
        if n % i == 0:
            return False
        else: 
            i += 2

    return True
def primos_entre(a, b):
    i = a
    n = 0
    while i <= b:
        if eh_primo(i) == True:
            n += 1
            i += 1
        else:
            i += 1
    return n