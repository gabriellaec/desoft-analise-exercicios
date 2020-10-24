

def eh_primo(a):
    if a > 2 and a != 3:
        n = 2
        divisor = 3
        while divisor < a:
            if a % 2 == 0:
                return False
            elif a % divisor == 0:
                divisor += n
                return False
            else:
                return True                
    else:
        if a == 2 or a == 3:
            return True
        else:
            return False