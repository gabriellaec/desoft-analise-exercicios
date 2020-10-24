a=True
while a:
    a=input("Código está executando?")
    if a=='n':
        print("Corrija o código e tente de novo")
    elif a=='s':
        b=input("O código produz o resultado correto?(n/s)")
        if b=='n':
            print("Corrija o código e tente de novo e volte para o começo de tudo")
        elif b=='s':
            print("Parabéns!")

