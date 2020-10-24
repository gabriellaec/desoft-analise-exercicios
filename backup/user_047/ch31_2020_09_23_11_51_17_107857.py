def eh_primo(x):
    contador = 2
    if x ==2:
        return False
    if x==1:
        return False
    if x==0:
        return False
    while contador<x:
        resto = x%contador
        contador += 1
        if resto ==0:
            return False
        else:
            return True
