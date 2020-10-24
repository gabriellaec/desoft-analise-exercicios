def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i < n:
        if n % i == 0:
            return False
        i += 2
    return True

def primos_entre(a,b):
    f = a
    i = 0
    while f <= b:
        if eh_primo(f):
            i+=1
        f+=1
    return i