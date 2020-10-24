# Define uma variável de estado
senha = True

# Define a condição do loop (enquanto a variável de estado é True)
while senha:
    resposta = input('digite a senha: ')
    if resposta != 'desisto':
        senha = True
    else:
        senha = False
print('Você acertou a senha!')      
 
