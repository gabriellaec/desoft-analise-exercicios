pal = input("Digite a senha ")
teste = True

while teste:
    if pal == "desisto":
        print("Você acertou a senha!")
        teste = False 
    else:
        pal = input("Digite a senha ")