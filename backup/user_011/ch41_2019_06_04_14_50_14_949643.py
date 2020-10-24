senha_certa = 'desisto' 

senha = True

while senha:
    pergunta_senha = input('Qual a senha? ')        
    if pergunta_senha == senha_certa:
        print('Voce acertou a senha!')
        senha = False

