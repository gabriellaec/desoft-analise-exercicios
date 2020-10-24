senha = 'desisto'
tentativa = input('Tente acertar a senha: ')
while tentativa != senha:
    tentativa = input('Senha errada, tente novamente: ')
print('Você acertou a senha!')