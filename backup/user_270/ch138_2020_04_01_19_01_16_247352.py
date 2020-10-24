k = True
while k:
    per1 = input("Código está executando?")
    if per1 == "s" :
        per2 = input("o código produz o resultado correto? ")
        if per2 == "s":
            print("Parabéns!")
            k = False
        if per2 == "n":
            print("Corrija o código e tente de novo e volte para o começo de tudo")
    if  per1 == "n" :
        print("Corrija o código e tente de novo")