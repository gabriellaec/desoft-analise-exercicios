resultado = ""

while resultado != "s":
    executando = input("Código está executando?(s/n) ")
    if executando == "n":
        print("Corrija o código e tente de novo")   
    if executando == "s":
        resultado = input("Produz o resultado correto?(s/n) ")
        if resultado == "n":
            print("Corrija o código e tente de novo e volte para o começo de tudo")
        if resultado == "s":
            print("Parabéns!")