def eh_primo(num):
    for n in range(3,num,2):
        if num%2==0 or num%n==0:
            return False
    if num==0 or num==1:
        return False
    
    elif num%2!=0 or num%n!=0 or n!=1:
        return True