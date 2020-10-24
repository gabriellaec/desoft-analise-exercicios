def eh_primo(num):
    i=num-2
    while i>=1:
        if num%i!=0 and num%2!=0 or num==2 or num!=1 or num!=0:
            i-=2
        else:
            return False
    return True
            