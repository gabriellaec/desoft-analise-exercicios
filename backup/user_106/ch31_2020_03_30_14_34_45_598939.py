i=3

def eh_primo(n):
    if n%2==0:
        return False
    else:
        while i<n:
            if n%i==0:
                return False
            i+=2
        return True