import random
player_money = 100
sorteio = random.randint(0,36)
while player_money > 0:
    print('\nVocê tem {0} dinheiros'.format(player_money)) 
    aposta = int(input('Quanto deseja apostar?'))
    if aposta == 0:
        break
    else: 
        opcao = input('\nDeseja apostar em número ou paridade? (n/p) ')
        if opcao == 'n':
            n = int(input('Digite um número de 1 a 36: '))
            if n == sorteio:
                player_money += n*aposta
                print('Parabéns, ganhou!')
            else:
                player_money -= aposta
                print('Perdeu :(')
        else:
            escolha = input('Deseja escolher par ou ímpar? (p/i) ')
            if escolha == 'p':
                if sorteio%2==0:
                    player_money += aposta
                    print('Parabéns, ganhou!')
                else:
                    player_money -= aposta
                    print('Perdeu :(')
            else:
                if sorteio%2 != 0 :
                    player_money += aposta
                    print('Parabéns, ganhou!')
                else:
                    player_money -= aposta
                    print('Perdeu :(')