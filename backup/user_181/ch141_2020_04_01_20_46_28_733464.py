import random
din = 1000
while True:
    print('voce tem essa quantia de dinheiro: {0} '.format(din))
    if din <= 0:
        break
    aposta = input('quer apostar?')
    if aposta == 'não':
        print('Você terminou a partida com {0} dinheiros'.format(din))
        break
    else:
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma = dado1 + dado2
        chute = input('advinhe a soma dos dados')
        din -= 30
        if chute == soma:
            print('vc acertou')
            din += 50
            print('Você terminou a partida com {0} dinheiros'.format(din))
            continue
        elif chute != soma:
            print('vc errou')
            continuar_ou_desistir = input('quer continuar ou desistir?')
            if continuar_ou_desistir == 'desistir':
                print('Você terminou a partida com {0} dinheiros'.format(din))
                continue
            elif continuar_ou_desistir == 'continuar':
                chute = input('advinhe a soma dos dados')
                din -= 20
                if chute == soma:
                    print('vc acertou')
                    din += 50
                    print('Você terminou a partida com {0} dinheiros'.format(din))
                    continue
                elif chute != soma:
                    print('vc errou')
                    print('o valor do primeiro dado eh {0}'.format(dado1))
                    continuar_ou_desistir = input('quer continuar ou desistir?')
                    if continuar_ou_desistir == 'desistir':
                        print('Você terminou a partida com {0} dinheiros'.format(din))
                        continue
                    elif continuar_ou_desistir == 'continuar':
                        din -= 10
                        chute = input('advinhe a soma dos dados')
                        if chute == soma:
                            print('vc acertou')
                            din += 50
                            print('Você terminou a partida com {0} dinheiros'.format(din))
                            continue
                        else:
                            print('vc errou')
                            continue
