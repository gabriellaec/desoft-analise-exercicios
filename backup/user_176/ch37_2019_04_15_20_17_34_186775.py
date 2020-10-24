def lista_primos(n):
    lista=[0]*n
    h=1
    j=0
    def eh_primo(h):
        primo = True
        divisor = 2
        if h<2:
            primo = False
        elif h==2:
            primo = True
        else:
            while divisor<h:
                if h%divisor == 0:
                    primo = False
                divisor+=1
        return primo
    if eh_primo(h) == True:
        lista[j]=h
        j+=1
    return lista
    