def eh_primo(n):
    if n<2:
        return False
    elif n==2:
        return True
    for x in tange(2,n):
        if n%x==0:
            return True
    return True
        