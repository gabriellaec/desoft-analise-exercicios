def eh_primo(x):
    contador = 0 
    x = 0
    while contador<x:
        resto = x%contador
        x = resto
        contador += 1
    if resto ==0:
        return False
    else:
        return true 