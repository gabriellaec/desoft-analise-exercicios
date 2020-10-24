def eh_primo(n):
    if n <= 1:
        return False
    
    np = 3
    while np < n:
        
        if n%2 == 0 or n%np == 0:
            return False
        np +=2
    return True 

def primos_entre(a, b):
    primos_e = []
    while a <= b:
        if eh_primo(a) == True:
            primos_e.append(a)
        a+=1
    return primos_e