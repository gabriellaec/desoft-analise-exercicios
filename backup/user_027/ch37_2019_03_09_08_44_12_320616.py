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
def imprime_primos(x):
    var = 1
    while var <= x:
        if eh_primo(var):
            print(var)
            var = var + 1
        else:
            var = var + 1
n = int(input('Digite um número: '))