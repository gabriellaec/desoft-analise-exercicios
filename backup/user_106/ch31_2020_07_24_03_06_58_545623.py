def eh_primo(n):
    if n < 2 or n % 2 == 0:
        return False
    elif n==2:
        return True
    else:
        i=3
        while i<n:
            if n%i==0:
                return False
            i+=2
        return True