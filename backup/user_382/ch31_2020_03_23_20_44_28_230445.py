def eh_primo(num):
    div = 3 
    if num % 2 == 0 and num != 2 or num == 1 or num == 0:
        return False
    
    while num > div:
        if num % div == 0:
            return False
        div += 2 
    return True 
