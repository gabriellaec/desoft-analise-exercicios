def eh_primo (num):
    if num < 2 or num % 2 == 0:
        return False
    else:
        i = 3
        while i < num:
            if num % i == 0:
                return False
            else:
                break
            i += 2

    return True
