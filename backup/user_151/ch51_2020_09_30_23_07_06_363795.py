def eh_primo(x):
    if x == 0 or x == 1:
        return False
    elif x % 2 == 0 and x != 2:
        return False
    elif x == 2 or x == 3:
        return True
    else:
        z = 1
        y = 2*z + 1
        while y < x:
            if x % y == 0:
                return False
                break
            else:
                z = z + 1
                y = 2*z + 1
        if x == y:
            return True

def primos_entre(a, b):
    i = a
    y = []
    while i<=b:
        if eh_primo(a):
            y.append(a)
        i = i + 1
    return y


