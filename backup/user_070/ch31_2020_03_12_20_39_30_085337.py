def eh_primo(n):
    i=3
    if n==2 or n==3:
        return True
    elif n%2==0 or n==1 or n==0:
        return False
    else:
        while n%i!=0 and n>i:
            i+=2
        if n==i:
            return True
        else:
            return False