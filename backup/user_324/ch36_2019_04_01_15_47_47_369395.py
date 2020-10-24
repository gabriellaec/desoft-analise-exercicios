def eh_primo(num):
    n=3
    while n<num:
        if num%2==0 or num%n==0:
            return False
        n+=2
    if num%2!=0 or num%n!=0:
        return True
    
    