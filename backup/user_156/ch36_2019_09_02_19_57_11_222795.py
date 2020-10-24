i=1
def eh_primo(x):
    while x != 0:
        i+=2
        a = x/2 and x/i
        if a != 0:
            return True
        else:
            return False
            
            
    