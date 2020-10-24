acertou = False
while acertou == False:
    palavra = str(input("Tente adivinhar a palavra: "))
    if palavra == "desisto":
        print("Você acertou a senha!")
        acertou = True
    else:
        print("Você errou. Tente novamente")
        acertou == False