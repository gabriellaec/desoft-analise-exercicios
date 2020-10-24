def eh_primo(n):
    if n==0 or n==1:
        return False
    else:
        divisor=0
        for x in range(1,n):
            if n%x==0:
                x=divisor+1
                divisor+=1
        			if divisor>=2:
            			return False
        			else:
            			return True
print(primo(3))