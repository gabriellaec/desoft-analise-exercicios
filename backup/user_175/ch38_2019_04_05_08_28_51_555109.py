from math import sqrt

def eh_primo(x):
    x = int(x)
    if x == 2:
        return True
    elif x < 2:
        return False
    t = 2
    while t <= sqrt(x):
        if x % t == 0:
            return False
        elif x % t !=0:
            t += 1
    return True

def primos_entre(x,y):
    x = int(x)
    y = int(y)
    var = x
    numb = 1
    while var <= y:
        if eh_primo(var):
            print('# {0} ----> {1}'.format(numb,var))
            var = var + 1
            numb = numb + 1
        else:
            var = var + 1
    return (numb)