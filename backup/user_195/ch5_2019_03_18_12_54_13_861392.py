def teste_primo(n):
    i=1
    p=0
    metade=n/2
    while i<=n:
        if n%2==0:
            p=1
            break
        if n%i==0:
            i+=1
            p+=1
        if i>=metade:
            i=n
            p+=1
            i+=1
        else:
            i+=1
    if p==2:
        return True
    else:
        return False

def eh_primo(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    else:
        return teste_primo(n)
    
logico=0    
def maior_primo_menor_que(n):
    if eh_primo(n)==True:
        return n
    elif n<2:
        return "-1"
    else:
        while eh_primo==False:
            logico=n
            n-=1
            return teste_primo(n)
        return logico
