def eh_primo(num):
    if num%2==0:
        i=num-1
    else:
        i=num-2
    while i>1:
        if num%i!=0 and num%2!=0 and num!=0 and num!=1 or num==2:
            i-=2
        else:
            return False
    return True


    