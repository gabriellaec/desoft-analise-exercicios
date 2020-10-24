def eh_primo(x):
    contador = 1 
    resto = 0 
    z = 0
    while contador<x:
        resto = x%contador
        contador += 1
        z = resto + z
    if z ==0:
        return False
    else:
        return true 
