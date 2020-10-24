def eh_primo(x):
    if x == 2:
        return True
    elif x == 1 or x == 0:
        return False
    y=3
    while x>2:
        if x%2 == 0:
            return False
        elif x == y:
            return True
        elif x>y and x%y == 0:           
            return False            
        else:
            y+=2
    return True

def primos_entre (a,b):
    p=0
    i=0
    while i<=b-a:
        if eh_primo(i) == True
            p += 1
        else:
            i+=1
    return p