def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    
    for test in range(3, n, 2):
        if n % test == 0:
            return False
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