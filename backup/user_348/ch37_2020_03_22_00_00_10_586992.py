senha = True
 
while senha:
    resposta = input('digite a senha: ')
    if resposta != 'desisto':
        senha = True
    else:
        senha = False
print('Você acertou a senha!')      
 
