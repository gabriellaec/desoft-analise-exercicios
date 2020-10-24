def eh_primo(n):
    if n == 0 or n==1:
        return False
    for c in range(2, n):
        if c % 2 != 0 or c == 2:
            print(c)
            if n % c == 0:
                return False
    return True

def primos_entre(a, b):
    l = []
    for c in range(a, b+1):
        l.append(c) if eh_primo(c) else pass
    return l