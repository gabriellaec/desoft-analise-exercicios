def eh_primo(x):
    contador = 2
    z = 2
    if x ==2:
        return True
    if x==1:
        return False
    if x==0:
        return False
    while z !=0:
        resto = x%contador
        z = resto
        if z == 0:
            return False
        else:
            contador+=1
            resto = x%contador
            if resto != 0:
                return True
