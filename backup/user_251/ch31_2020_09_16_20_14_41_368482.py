n = 0
divisor = 2*(n+1)
def eh_primo(a):
    if a > 1:
        n = 0
        divisor = 2*(n+1)
        while divisor < a:
            if a % divisor == 0:
                divisor += 1
                n += 1
                return False
            else:
                return True
    else:
        if a == 1:
            return True
        else:
            return False

print(eh_primo(1))
        
            