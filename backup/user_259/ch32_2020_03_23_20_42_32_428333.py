def eh_primo(p):
    i = 3
    if n<=1:
        return False
    if n%2==0:
        if n==2:
            return True
        else:
            return False
    else:
        while i<n:
            if n%i==0:
                return False
            else:
                i+=2
        return True
def lista_primos(n):
	lista = []
	c=0
	while c<n:
        if eh_primo(p)==True:
            lista.append(p)
            p+=1
            c+=1
        else:
            p+=1
            return lista