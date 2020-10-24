contador=3
def eh_primo(n):
    if n==0 or n==1 or n==2:
        return "eh primo"
    elif n%2=0:
    	return "Não é primo"
    else:
        while contador<=n:
            if n%contador=0:
                return "Não é primo"
            contador +=2
            else:
                return "eh primo"