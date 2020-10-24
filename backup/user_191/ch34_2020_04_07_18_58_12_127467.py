def eh_primo(n):
    if n<=1:
        return(-1)
    elif n==2:
        return(2)
    else:
        while eh_primo:
            divisores = 0
            for divisor in range(1, n):
                if n % divisor == 0:
                    divisores = divisores + 1
            if divisores > 1:
                n=n-1
            else:
                return (n)