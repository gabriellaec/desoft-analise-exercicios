def eh_primo(n):
    if n == 0 or n ==1:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        x = 3
        while x<n:
            if n % x ==0:
                return False
            x = x+2
        if x == n:
            return True
        else:
            return False
            