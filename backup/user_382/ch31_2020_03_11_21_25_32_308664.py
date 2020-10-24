div = 3

def eh_primo(num):
    if num % 2 ==0 and num != 1 and num != 0:
        return False 

    while num < div:
        if num % div == 0:
            return False 
    
    return True 
    