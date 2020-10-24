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
def eh_primo(num):
    n=3
    while n<num:
        if num%2==0 or num%n==0:
            return False
        n+=2
    if num==0 or num==1:
        return False
    
    elif num%2!=0 or num%n!=0 or n!=1:
        return True
    