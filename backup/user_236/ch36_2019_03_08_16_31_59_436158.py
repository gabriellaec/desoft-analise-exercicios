def eh_primo(n):
    if n==1 or n==0:
        return false
    else:
         x=n-1
        while x<1:
            if n%x==0:
                return False
            x-=1
        return true
