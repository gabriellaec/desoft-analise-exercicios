def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i >= 3:
        if i % 2 ==0:
            continue
        else:
            if n % i ==0:
                return False
        i+=1
