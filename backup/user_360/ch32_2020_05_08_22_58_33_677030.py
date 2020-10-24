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
def lista_primos(n):
    lista = []
    x = 0
    while True:
        y = eh_primo(x)
        if y == True:
            lista.append(x)
        if len(lista) == n:
            break
        x+=1
    return lista
    