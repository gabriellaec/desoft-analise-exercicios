def eh_primo (x):
    if x==2:
        return True
    elif x==1 or x==0:
        return False
    elif x%2==0:
        return False
    else:
        n = 3
        while n < x:
            if x%n==0:
                return False
            n=n+2
        else: 
            return True
def primos_entre(x,y):
    primos = []
    while x != y+1:
        if eh_primo(x) == True:
            primos.append(x)
            
        x = x + 1
    return primos
