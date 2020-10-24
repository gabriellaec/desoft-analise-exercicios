def eh_primo(numero):
    n=2
    while n<=numero:
        if numero%2 != 0:
            d=3
            while d<numero:
                if numero%d==0:
                    print("Não é primo")
                    d+=2
                else:
                    print("É primo")
        else:
            print("Não é primo")