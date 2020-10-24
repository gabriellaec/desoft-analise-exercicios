def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    for i in range(3, n, 2):
        if n%2==0:
            return False
        elif n%i==0:
            return False
    else:
        return True
    
def primos_entre(a, b):
    q = 0
    d = a+1
    if b-a ==1:
        return 2
    else:
        while d<b:
            if eh_primo(d):
                q+=1
            d+=1
        return q
    
    
    