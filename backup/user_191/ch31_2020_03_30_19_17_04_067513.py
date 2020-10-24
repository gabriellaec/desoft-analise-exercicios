def eh_primo(n):
    if n==0 or n==1:
        return 1>2
    elif n==2:
        return 1<2
    else:
        divisores = 0
        for divisor in range(3, n):
            if n % divisor == 0:
                divisores = divisores + 1
                if divisores > 1:
                    break
        if divisores > 1:
            return 1>2
        else:
            return 1<2