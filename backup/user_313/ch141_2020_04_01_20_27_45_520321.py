import random

dinheiros = 1000
dado1 = 0
dado2 = 0
resposta = 0
chute = 0
again = 0
novoChute = 0
again2 = 0
chute3  = 0

while True:
    pergunta = input('Você quer apostar ? ')
    
    if pergunta == 'não':
        print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
        break

    if pergunta != 'não':
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        resposta = dado1 + dado2

        chute = int(input('Qual a soma dos dados: '))

        dinheiros = dinheiros - 30

        if chute == resposta:
            dinheiros = dinheiros + 50
            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
            continue

        else:
            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
            again = input('Desejar continuar tentando ou vai desistir ? ')

            if again == 'desistir':
                continue

            else:
                dinheiros = dinheiros - 20
                novoChute = int(input('Qual a soma dos dados: '))

                if novoChute == resposta :
                    dinheiros = dinheiros + 50
                    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                    continue

                else:
                    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                    print('dado1 {0}'.format(dado1))
                    again2 = input('Desejar continuar tentando ou vai desistir ? ')

                    if again2 == 'desistir':
                        continue

                    elif again2 != 'desistir':
                        dinheiros = dinheiros - 10
                        chute3 = int(input('Qual a soma dos dados: '))
                        
                        if chute3 == resposta:
                            dinheiros = dinheiros + 50
                            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                            continue

                        else:
                            
                            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                            continue