def eh_primo(n):
    if (n == 0) or (n == 1):
        return False
    elif n == 2:
        return True
    else:
        i = n-2
        if n % 2 == 0:
            return False
        while i>1:
            if n % i == 0:
                return False
            i -= 2
            if i == 0:
                return True
        return True
def primos_entre(a, b):
    soma = 0
    for n in range(a+1, b, -2):
        if eh_primo(n) == True:
            if p % n != 0:
                if p >= a and p <= b:
                    soma += 1
    return soma