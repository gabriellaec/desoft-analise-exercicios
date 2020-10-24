pergunta= (input("Digite a senha correta!"))
tentativa= "Tente novamente"
i=True
while i:
    if pergunta=="desisto":
        print("Você acertou a senha!")
        i= False
    else:
        i= True