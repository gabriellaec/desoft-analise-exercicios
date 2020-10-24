

def eh_primo(a):
    divisor = 2
    if a == 2:
        return True
    while a % divisor != 0 and divisor <= a/2:
        divisor +=1
    if a % divisor == 0:
        return False
    else:
        return True
