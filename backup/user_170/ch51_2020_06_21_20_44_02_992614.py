e i < n:
            if n%i==0:
                return False
            i += 2
        return True


def primos_entre(a,b):
    primos = []
    for i in range(a,b+1):
        result = eh_primo(i)
        if result == True:
            primos.append(i)
    return primos