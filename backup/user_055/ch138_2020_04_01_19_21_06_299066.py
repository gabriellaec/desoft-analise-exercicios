correto = "n"
while correto == "n":
    exe = input("Código está executando?")
    if exe == "n":
        print("Corrija o código e tente de novo")
        while exe == "n":
            exe = input("Código está executando?")
            print("Corrija o código e tente de novo")
    if exe == "s":
        correto = input("O código produz o resultado correto?")
    if correto == "n":
        print("Corrija o código e tente de novo e volte para o começo de tudo")
    if correto == "s":
        break
print("Parabéns!")