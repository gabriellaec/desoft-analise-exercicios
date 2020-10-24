def eh_primo (x):
    if x == 2:
        return True
    elif x == 0 or x == 1 or x %2 == 0:
        return False
    i = 3
    while i < x:
        if x %i == 0:
            return False
        else:
            i += 2
def primos_entre (a, b):
    i = a
    n = []
    while i <= b:
        if eh_primo(i) == True:
            n.append(i)
            i += 1
        else:
            i += 1
    return n