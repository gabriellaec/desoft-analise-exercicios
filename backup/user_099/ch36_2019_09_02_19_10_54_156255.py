i=3
def eh_primo(num):
    if num==0 or num==1:
        return False
    elif num==2:
        return True
    else:
		while i<num:
            if num%i==0:
                resto = num%i
            	break
            else:
                i=i+2
                resto = num%i
        if resto ==0:
            return True
        else:
            return True