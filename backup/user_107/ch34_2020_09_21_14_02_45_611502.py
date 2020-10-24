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


def maior_primo_menor_que (num):
    num -= 1
    while num > 1:
        if eh_primo(num):
            return num
        num -= 1
    return -1