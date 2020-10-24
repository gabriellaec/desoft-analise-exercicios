def calcula_primo(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
            else:
                return True
            break
    else:
        return False