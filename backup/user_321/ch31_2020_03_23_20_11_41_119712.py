def eh_primo(n):
    i = 3
    if n == 2:
        return True
    elif n == 1 or n == 0:
        return False
    elif(n%2==0):
        return False
    else:
        while (i<n):
            if (n%i==0):
                return False
            else:
                i = i+2
        return True