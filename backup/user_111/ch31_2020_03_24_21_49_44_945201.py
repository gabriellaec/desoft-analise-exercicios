def eh_primo(numero):
    n=2
    while n <= numero:
        if n%2 != 0:
            d=3
            while d<numero:
                d+=2
                if numero%d==0:
                    print("Não é primo")
                else:
                    print("É primo")