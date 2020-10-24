def eh_primo(n):
    if n/2==0:
        return False
    else:
        d=3
        while n>d:
            if n/d==0:
                return False
            else:
                d+=2
		return True
            
        