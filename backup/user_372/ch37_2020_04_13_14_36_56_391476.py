senha='desisto'
acertou=False
while acertou==False:
    palavra=str(input('Digite a senha: '))
    if palavra!=senha:
        print('Você errou, tente novamente.')
    else:
        print('Você acertou a senha!')
        acertou=True
