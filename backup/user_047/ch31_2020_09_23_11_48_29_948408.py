def eh_primo(x):
    contador = 2
    if x ==2:
        return True
    while contador<x:
        resto = x%contador
        contador += 2
        if resto ==0:
            return False
        else:
            return True
a = eh_primo(5)
print(a)

