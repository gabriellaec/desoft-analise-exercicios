def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    while True:
        i = n-1
        if i % 2 ==0:
            continue
        if i % 2!=0:
            if n % i == 0:
                return False
            else:
                continue
                
