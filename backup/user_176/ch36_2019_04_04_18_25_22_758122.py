def eh_primo(n):
    primo = True
    divisor = 2
    if n < 2:
        primo = False
    elif n == 2:
        primo = True
    else:
        while divisor < n:
            if n%divisor == 0:
                primo = False
            divisor += 1
    return primo