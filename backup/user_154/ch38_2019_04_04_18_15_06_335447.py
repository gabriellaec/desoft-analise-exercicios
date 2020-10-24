def eh_primo(n):
    if n < 2:
        return False
    test = 2
    while(test < n):
        if ((n % test) == 0):
            return False
        test = test + 1
    return True

def primos_entre(a,b):
    result = []
    
    while a <= b:
        if eh_primo(a):
            result.append(a)
        a = a + 1
        
    return len(result)