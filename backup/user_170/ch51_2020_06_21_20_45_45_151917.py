def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n%2==0 and n!=2:
        return False
    else:
        i = 3
        while i < n:
            if n%i==0:
                return False
            i += 2
        return True


def primos_entre(a,b):
    primos = []
    for i in range(a,b+1):
        if i >= 0:
            result = eh_primo(i)
            if result == True:
                primos.append(i)
    return primos