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


def primos_entre (a, b):
    result = []
    number = a

    while number < b:
        if eh_primo(number):
            result.append(number)
        number += 1

    return result