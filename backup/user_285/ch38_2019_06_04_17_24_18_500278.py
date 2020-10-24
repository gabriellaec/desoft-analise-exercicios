def eh_primo(num):
    n=3
    while n<num:
        if num%2==0 or num%n==0:
            return False
        n+=2
    if num==0 or num==1:
        return False
    
    else:
        return True
    
def primos_entre(a,b):
    c=0
    for X in range(a,b+1):
        if eh_primo(X):
            c+=1
    return c
    