x = True

while x == True:
    y = input("Código está executando?")
    while y != "s":
        print("Corrija o código e tente de novo")
        y = input("Código está executando?")
    if y == "s":
        z = input("O código produz o resultado correto?")
        if z == "n":
            print("Corrija o código e tente de novo")
            y = "n"
        elif z == "s":
            x = False

print("Parabéns!")
