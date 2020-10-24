def eh_primo(n):
    if n==0 or n==1:
        return "Não é primo"
    else:
        divisor=0
        for x in range(1,n):
            if n%x==0:
                x=divisor+1
                divisor+=1
        			if divisor>=2:
            			return "Não é primo"
        			else:
            			return "É primo"