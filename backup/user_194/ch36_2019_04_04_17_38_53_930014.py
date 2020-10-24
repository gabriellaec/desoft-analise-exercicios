def eh_primo(n):
    primo = true
    divisor = 2
    if n < 2:
        primo = false
    elif n == 2:
        primo = true
    else:
        while divisor < n:
            if n % divisor == 0:
                primo = false
            divisor += 1
    return primo