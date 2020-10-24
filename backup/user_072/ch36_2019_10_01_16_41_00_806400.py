def eh_primo(n):
    if n==0 or n==1:
        return False
    if n==2:
        return True
    i=3
    while n>i:
        if n%2==0 or n%((i*2)+1)==0:
            i+=1
            return False
        else:
            return True
    return False