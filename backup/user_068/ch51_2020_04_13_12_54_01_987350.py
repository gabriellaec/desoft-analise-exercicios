def eh_primo(num):
    i = 2 
    if num == 2:
        return True
    elif num == 0 or num == 1:
        return False
    while i < num:
        if num % i == 0:
            return False
        i = i + 1
    return True
def primos_entre(a, b):
    c = []
    for p in range(a, b+1):
        eh_primo(p) and c.append(p)
    return c
        
 