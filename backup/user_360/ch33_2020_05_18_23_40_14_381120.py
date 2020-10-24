def eh_primo(p):
    if p<2:
        return False 
    elif p==2:
        return True 
    elif p%2==0:
        return False
    else:
        n=3
        while n<p:
            if p%n==0:
                return False
            n+=2
        return True
def primos_entre(a, b):
    i = 0
    cont = b
    while cont>=a:
        x = eh_primo(cont)
        if x == True:
            i +=1
        cont = cont-1
    return i