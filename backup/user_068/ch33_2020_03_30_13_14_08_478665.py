def eh_primo(n):
    c=2
    if n == 0 or n==1:
        return False
    while c < n:
        if n % c == 0:
            return False
        c += 1
    
    return True

def primos_entre(a, b):
    num = 0
    c = a
    while c <= b:
        if eh_primo(c):
            num += 1
        c += 1
    return num
   