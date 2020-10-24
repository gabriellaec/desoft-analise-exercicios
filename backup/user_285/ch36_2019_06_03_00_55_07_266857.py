def eh_primo(n):
    if n==2:
        return True
    if n==0 or n==1:
        return False
    for i in range(3,n+1,2):
        if n%2==0:
            return False
        if n%i==0:
            return False
        else: 
            return True
