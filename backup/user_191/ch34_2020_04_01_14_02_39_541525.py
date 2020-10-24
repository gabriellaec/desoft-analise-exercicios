def maior_primo_menor_que(n):
    def eh_primo(n):
        if n==0 or n==1:
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
    if eh_primo:
        return(n)
    else:
        n=n-1