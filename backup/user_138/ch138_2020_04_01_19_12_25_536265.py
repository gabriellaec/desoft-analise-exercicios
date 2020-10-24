executando=True
while executando:
    executando=input("Código está executando?")
    if executando!="s":
        print("Corrija o código e tente de novo")
    elif executando=="s":
        correto=input("Produz o resultado correto?(n/s)")
        if correto=="n":
            print("Corrija o código e tente de novo e volte para o começo de tudo")
        else:
            print("Parabéns!")