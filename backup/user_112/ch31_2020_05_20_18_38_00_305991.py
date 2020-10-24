def eh_primo(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n > 1:
        for i in range(2, n):
            if i % 2 == 0:
                return False
            else: 
                return True
    