import random
dinheiro = 1000
aposta = True
while aposta:
    p_apostar = input('Você deseja apostar?')
    if p_apostar == 'não':
        print('Você terminou a partida com {0} dinheiros.'.format(dinheiro))
        aposta = False
    else:
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma_dados = dado1 + dado2
        chute = int(input('Qual a soma dos dados?'))
        dinheiro = dinheiro - 30
        if chute == soma_dados:
            dinheiro = dinheiro + 50
            print('Você terminou a partida com {0} dinheiros.'.format(dinheiro))
        else:
            continuar_desistir = input('Você deseja continuar a apostar ou desistir?')
            if continuar_desistir == 'desistir':
                print('Você terminou a partida com {0} dinheiros.'.format(dinheiro))
            else:
                chute2 = int(input('Qual a soma dos dados?'))
                dinheiro = dinheiro - 20
                if chute2 == soma_dados:
                    dinheiro = dinheiro + 50
                    print('Você terminou a partida com {0} dinheiros.'.format(dinheiro))
                else:
                    print(dado1)
                    continuar_desistir = input('Você deseja continuar a apostar ou desistir?')
                    if continuar_desistir == 'desistir':
                        print('Você terminou a partida com {0} dinheiros.'.format(dinheiro))
                    else:
                        chute3 = int(input('Qual a soma dos dados?'))
                        dinheiro = dinheiro - 10
                        if chute3 == soma_dados:
                            dinheiro = dinheiro + 50
                            print('Você terminou a partida com {0} dinheiros.'.format(dinheiro))
                        else:
                            print('Você terminou a partida com {0} dinheiros.'.format(dinheiro))
