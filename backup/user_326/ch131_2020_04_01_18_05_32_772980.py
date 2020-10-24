import random 

dado1 = random.randint(1, 10)
dado2 = random.randint(1, 10)
soma_dados = dado1 + dado2
creditos = 10

print('Fase de dicas')
pergunta_dica1 = int(input('Chute um número: '))
pergunta_dica2 = int(input('Chute outro número maior ou igual ao anterior: '))
if pergunta_dica1 > soma_dados:
    print('Soma menor')
elif pergunta_dica2 < soma_dados:
    print('Soma maior')
else:
    print('Soma no meio')

print('Fase de chutes')
print('Você tem {} dinheiros disponíveis'.format(creditos))
quantos_chutes_voce_quer = int(input('Quantos inputs você quer comprar? 1 input custa 1 dinheiro. '))
creditos -= quantos_chutes_voce_quer
while quantos_chutes_voce_quer > 0:
    chute = int(input('Chute um número: '))
    if chute == soma_dados:
        creditos = creditos + creditos * 5
        print('Parabéns você acertou!')
        break
    else:
        quantos_chutes_voce_quer -= 1
        print('Você errou, tente novamente.')
print('Você terminou o jogo com {} dinheiros'.format(creditos)