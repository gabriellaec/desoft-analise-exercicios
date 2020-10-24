def eh_primo (num):
    if num < 2 or num > 2 and num % 2 == 0:
        return False
    else:
        i = 3
        while i < num:
            if num % i == 0:
                return False
            i += 2

    return True

def lista_primos (n):
    result = [0] * n
    i = 0
    num = 2
    while i < n:
        if eh_primo(num):
            result[i] = num
            i += 1
        num += 1

    return result
