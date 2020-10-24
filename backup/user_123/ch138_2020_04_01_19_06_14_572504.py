a = 0
b = 0

while a == "n" and b == "n":
    a = input("O código está executando?(s/n)")
    print (a)
    if a =="n":
        print ("Corrija o código e tente de novo")
    elif a == "s":
        b = input("Produz o resultado correto?(s/n) ")
        if b == "n":
            print ("Corrija o código e tente de novo e volte para o começo de tudo")
        elif b == "s":
            print ("Parabens!")
            break
       