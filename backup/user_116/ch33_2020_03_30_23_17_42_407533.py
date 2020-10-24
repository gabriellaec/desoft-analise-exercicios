def eh_primo (n):
    if n == 2:
        return True
    elif n == 0 or n == 1:
        return False
    elif n%2 == 0:
        return False
    else:
        contador = 3
        while contador < n:
            if n%contador == 0:
                return False
            contador += 2    
        return True
def primos_entre(a,b):
    p=0
    while b-a>0:
        while eh_primo(a)==False and b-a>0:
            a+=1
        if eh_primo(a) == True:
            p+=1
        a+=1
    return p