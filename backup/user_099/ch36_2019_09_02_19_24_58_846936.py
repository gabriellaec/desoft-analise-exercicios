def eh_primo(num):
    a=3
    if num==0 or num==1:
        return False
    elif num==2 or num==3:
        return True
    elif num%2==0:
        return False
    else:
        while a<num:
            if num%a==0:
                resto = num%a
                break
            else:
                a=a+2
                resto = num%a
        if resto ==0:
            return False
        else:
            return True