def eh_primo(x):
    i = 2
    while i <= x:
        a = x%2 
        b = x%i
        if a == 0 or b == 0:
            return False
        elif x == 0 or x == 1:
            return False
        else:
            return True
        i += 1