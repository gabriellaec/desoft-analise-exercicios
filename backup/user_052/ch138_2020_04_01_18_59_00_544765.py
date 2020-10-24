perg = True
while perg:
    perg = input ("Código está executando?")
    if perg == "n":
        print ("Corrija o código e tente de novo")
    elif perg == "s":
        perg2 = input("O código produz o resultado correto?")
        if perg2 == "n":
            print ("Corrija o código e tente de novo e volte para o começo de tudo")
        elif perg2 == "s":
            print ("Parabéns")