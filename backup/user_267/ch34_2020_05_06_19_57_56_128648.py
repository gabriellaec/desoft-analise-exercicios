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
def maior_primo_menor_que(n):
    a = 0
    maior = 0
    if eh_primo(a) == True:
        if a > maior:
            maior = a
        a += 1
    else:
        return -1
