def eh_primo(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    i = 2
    while i < n:
        i = 3
  
        if n%i != 0:
            return True
        i = i+2
        
       	if n == i:
            return True
        else:
            return False