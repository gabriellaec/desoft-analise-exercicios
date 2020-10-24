#dinheiro inicial do jogador
player_money = 10

#Sorteio dos dados
import random
d1 = random.randint(1,6)
d2 = random.randint(1,6)
soma = d1+d2

##Fase de dicas
dicas = True
while dicas:
    print('Você tem {} dinheiros'.format(player_money))
    if player_money > 0:
        dica = input('Você quer uma dica? (sim/não) ')
        if dica == 'sim':
            player_money -= 1
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite um número: '))
            n3 = int(input('Digite um número: '))
            if soma == n1 or soma==n2 or soma==n3:
                print('Está entre os 3')
            else: 
                print('Não está entre os três')
        else: 
            dicas = False
    else: 
        dicas = False

## Fase chutes
chutes = True
while chutes:
    print('Você tem {} dinheiros'.format(player_money))
    if player_money>0:
        chute = int(input('Chute um número: '))
        if chute == soma:
            player_money += player_money*5
            chutes = False
        else:
            player_money -= 1 
    else:
        chutes = False

if player_money>0:
    print('Você ganhou o jogo com {0} dinheiros!'.format(player_money))
else:
    print('Você perdeu!')