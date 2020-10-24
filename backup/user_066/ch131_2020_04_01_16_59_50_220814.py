import random
dados = random.randint(1, 10) + random.randint(1, 10)
numero = int(input('Insira um numero para receber algumas dicas' ))
numero2 = int(input('Insira outro numero maior ou igual ao primeiro '))
soma_numero = numero + numero2
if soma_numero < dados:
    print('Soma menor')
elif soma_numero > dados:
    print('Soma maior')
else:
    print('Soma no meio')
dinheiros = 10
print('Você tem {0} dinheiros'.format(dinheiros))
numero_chutes = int(input('Quantos chutes deseja comprar? '))
dinheiros -= numero_chutes
while numero_chutes != 0:
    chute = int(input('Qual seu chute?' ))
    if chute == dados:
        dinheiros *= 4
        break
    else:
        numero_chutes -= 1
print('Você terminou o jogo com {0} dinheiros'. format(dinheiros))
        