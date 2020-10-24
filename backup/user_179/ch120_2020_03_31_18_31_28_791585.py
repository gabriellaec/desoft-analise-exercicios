from random import randint
jogo = True
while jogo:
    dinheiro = 100
    while dinheiro > 0:
        print ('Você tem R${0}'.format(dinheiro))
        aposta = int(input('Quanto você quer apostar? '))
        if aposta == 0:
            jogo = False
        else:
            jogo = True
        escolha = str(input('Quer apostar em um número ou em uma paridade?(n / p ou i) '))
        aleatorio = randint(0,36)
        if escolha == 'n':
            numero = int(input('Escolha um número entre 1 e 36: '))
            if numero == aleatorio:
                print ('Parabéns! Você ganhou!')
                dinheiro = dinheiro + (aposta * 35)
                print ('Agora você tem R${0}'.format(dinheiro))
            else:
                print ('Que pena! Você perdeu...')
                dinheiro = dinheiro - aposta
                print ('Agora você tem R${0}'.format(dinheiro))
        elif escolha == 'p':
            if (aleatorio % 2 == 0):
                print ('Parabéns! Você ganhou!')
                dinheiro = dinheiro + aposta
                print ('Agora você tem R${0}'.format(dinheiro))
            else:
                print ('Que pena! Você perdeu...')
                dinheiro = dinheiro - aposta
                print ('Agora você tem R${0}'.format(dinheiro))
        elif escolha == 'i':
            if (aleatorio%2==1):
                print ('Parabéns! Você ganhou!')
                dinheiro = dinheiro + aposta
                print ('Agora você tem R${0}'.format(dinheiro))
            else:
                print ('Que pena! Você perdeu...')
                dinheiro = dinheiro - aposta
                print ('Agora você tem R${0}'.format(dinheiro))
        else:
            print('Digite novamente alguma das opções listadas')