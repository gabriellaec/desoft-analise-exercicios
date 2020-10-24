def eh_primo(x):
    x = int(x)
    if x == 2:
        return True
    elif x < 2:
        return False
    t = 2
    while t < x:
        if x % t == 0:
            return False
        elif x % t !=0:
            t += 1
    return True
def imprime_primos(x,y):
    x = int(x)
    y = int(y)
    var = x
    cnt = x
    while var <= y:
        if eh_primo(var):
            print(var)
            cnt = cnt + 1
            var = var + 1
        else:
            var = var + 1