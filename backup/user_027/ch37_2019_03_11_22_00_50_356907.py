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
def imprime_primos(x):
    var = 1
    cnt = 1
    while cnt <= x:
        if eh_primo(var):
            print(var)
            cnt = cnt + 1
            var = var + 1
        else:
            var = var + 1
n = int(input('Digite um numero: '))
imprime_primos(n)
