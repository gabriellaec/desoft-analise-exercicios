n = int() 
def eh_primo(n):
    x = 3
    while x < (n - 2):
        x += 2
    if n % 2 == 0 and n != 2 or n % x == 0 and n != 3 or n == 0 or n == 1:
        return False
        
    else:
        return True
eh_primo(n)

