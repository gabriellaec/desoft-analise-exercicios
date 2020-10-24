def eh_primo(n):
    d=1
    while d<=n:
        if n%d==0:
            return False
        elif n % 2==0:
            return False
        else:
            return True
    d+=1