a = True
while a:
    resp = input("O código está executando? ")
    if resp == "n":
        print("Corrija o código e tente de novo")
    if resp == "s":
        resp2 = input("Produz o resultado correto? ")
        if resp2 == "n":
            print("Corrija o código e tente de novo")
        if resp2 == "s":
            print("Parabéns!")
            a = False 