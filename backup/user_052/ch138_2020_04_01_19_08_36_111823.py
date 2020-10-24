perg = True
while perg:
    perg = input ("Código está executando?")
    if perg == "n":
        print ("Corrija o código e tente de novo")
        perg = True
    elif perg == "s":
        perg2 = input("Produz o resultado correto?")
        perg = False
        if perg2 == "n":
            print ("Corrija o código e tente de novo e volte para o começo de tudo")
            perg = True
        elif perg2 == "s":
            print ("Parabéns!")
            perg = False