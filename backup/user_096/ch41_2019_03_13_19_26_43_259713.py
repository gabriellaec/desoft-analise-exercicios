tentativa = input('qual a senha?')
senha = "desisto"
game_on=True
while game_on:
    if tentativa!=senha:
        tentativa = input('errou, quala asenha ')
    elif tentativa==senha:
        print("Você acertou a senha!") 
        break

