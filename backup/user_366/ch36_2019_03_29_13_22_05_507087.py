def eh_primo(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        if n % 2 != 0: #Se der verdadeiro, ele é ímpar
            i = 3
            while i < n:
                a = n % i
                i += 2
            if a != 0:
                return True
            else:
                return False
        else:
            return False