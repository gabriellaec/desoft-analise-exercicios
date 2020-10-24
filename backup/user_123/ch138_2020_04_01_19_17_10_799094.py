t = True
while a == True:
    P1 = input("O código está executando?(s/n)"
    while P1 != "s":
    if P1 == "n":
        print ("Corrija o código e tente de novo")
    elif P1 == "s":
        P2 = input("Produz o resultado correto?(s/n) ")
        if P2 == "n":
            print ("Corrija o código e tente de novo e volte para o começo de tudo")
        elif P2 == "s":
            t = False
print ("Parabens!")

       