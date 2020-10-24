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
    count = 0
    num = 2
    while count < n:
        if eh_primo(num):
            print(num)
            count += 1
        num += 1
