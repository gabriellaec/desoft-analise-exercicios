teste= True
while teste:
    senha= input("Qual a senha ? ")
    if senha != "desisto":
        print ("você errou")
    elif senha == "desisto":
        print ("Você acertou a senha!")
        teste= False
    