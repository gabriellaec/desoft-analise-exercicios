from math import sqrt
def eh_primo(x):
    x = int(x)
    if x == 2:
        return True
    elif x < 2:
        return False
    t = 2
    while t < sqrt(x):
        if x % t == 0:
            return False
        elif x % t !=0:
            t += 1
    return True
def primos_entre(x,y):
    x = int(x)
    y = int(y)
    var = x
    lista = []
    while var <= y:
        if eh_primo(var):
            lista.append(var)
            var = var + 1
        else:
            var = var + 1
    return lista