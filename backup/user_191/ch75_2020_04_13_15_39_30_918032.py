def eh_primo(n):
    if n<=1:
        return 1>2
    elif n==2:
        return 1<2
    else:
        divisores = 0
        for divisor in range(1, n):
            if n % divisor == 0:
                divisores = divisores + 1
        if divisores > 1:
            return 1>2
        else:
            return 1<2
def verifica_primos(lista):
    dic={}
    for i in range(len(lista)):
        dic[lista[i]]=eh_primo(lista[i])
    return dic