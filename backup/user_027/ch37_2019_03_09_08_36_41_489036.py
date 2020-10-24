def eh_primo(x):
    x = int(x)
    if x == 2:
        return True
    elif x == 1:
        return False
    elif x == 0:
        return False
    t = 2
    while t < x:
        if x % t == 0:
            return False
        elif x % t !=0:
            t += 1
    return True

var = 1
n = int(input())
while var <= n:
    if eh_primo(var):
        print(var)
        var = var + 1
    else:
        var = var + 1
        