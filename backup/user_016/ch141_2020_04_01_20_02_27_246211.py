import random
game_on = True
print ('Você tem 1000 dinheiros')
while game_on:
    dinheiros = 1000
    pergunta1 = input('Você quer apostar? ')
    if pergunta1 == 'não':
        break
    else:
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma = dado1 + dado2
        chute1 = int(input('Chute um número para a soma dos dois dados. '))
        dinheiros = dinheiros - 30
        if chute1 == soma:
            dinheiros = dinheiros + 50
        else:
            pergunta2 = input('Você quer continuar tentando ou vai desistir? ')
            if pergunta2 == 'desistir':
                pass
            else:
                chute2 = int(input('Chute outro número para a soma dos dois dados. '))
                dinheiros = dinheiros - 20
                if chute2 == soma:
                    dinheiros = dinheiros + 50
                else:
                    pergunta3 = input('O valor de um dos dados é {0}, você quer continuar tentando ou vai desistir? '.format(dado1))
                    if pergunta3 == 'desistir':
                        pass
                    elif pergunta3 == 'continuar':
                        chute3 = int(input('Chute outro número para a soma dos dois dados. '))
                        dinheiros = dinheiros - 10
                        if chute3 == soma:
                            dinheiros = dinheiros + 50
                        else:
                            pass
    print('Você terminou a partida com {0} dinheiros'.format(dinheiros)) 
print('Você terminou a partida com {0} dinheiros'.format(dinheiros))           
