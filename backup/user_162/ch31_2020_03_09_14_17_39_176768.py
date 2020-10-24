def eh_primo(n):
    if n <= 1:
        return False
    
    np = 3
    while np < n:
        
        if n%2 == 0 or n%np == 0:
            return False
        np +=2
    return True 