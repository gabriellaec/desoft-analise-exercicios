pergunta_senha = input('Qual a senha? ')

senha_certa = 'facil demais' 

senha = True

while senha:
    if pergunta_senha != senha_certa:
        print(pergunta_senha)
    elif pergunta_senha == senha_certa:
        print('Voce acertou a senha!)
    elif pergunta_senha == "desisto"
         senha = False

