senha = True
while senha:
    leo = input("Qual é a palavra da senha?\n")
    if leo != "desisto":
        print ("Errou")
    else:
        senha = False
        print ("Você acertou a senha!")