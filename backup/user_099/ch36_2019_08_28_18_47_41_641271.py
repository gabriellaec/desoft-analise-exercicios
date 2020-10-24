i=3
def eh_primo(num):
    if num==0 or num==1:
        return False
    elif num==2:
        return True
    elif num%2==0:
        return False
    else:
		while i<num:
            if num%i==0:
                return False
            i=i+2
        return True