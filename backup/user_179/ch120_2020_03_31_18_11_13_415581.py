from random import randint
dinheiro = 100
jogo = True
while jogo:
    while dinheiro < 0:
        print ('Você ainda tem R${0}'.format(dinheiro))
        aposta = int(input('Quanto você quer apostar?'))
        if aposta == 0:
            jogo = False
        else:
            jogo = True
        escolha = str(input('Quer apostar em um número ou em uma paridade?(n/p ou i)'))
        if escolha == 'n':
            numero = int(input('Escolha um número entre 1 e 36: '))
            aleatorio = randint(1,36)
            if numero == aleatorio:
                print ('Parabéns! Você ganhou!')
                dinheiro = dinheiro + aposta * 35
                print ('Agora você tem R${0}'.format(dinheiro))
            else:
                print ('Que pena! Você perdeu...')
                dinheiro = dinheiro - aposta
                print ('Agora você tem R${0}'.format(dinheiro))
        elif escolha == 'p':
            if escolha%2==0:
                print ('Parabéns! Você ganhou!')
                dinheiro = dinheiro + aposta
                print ('Agora você tem R${0}'.format(dinheiro))
            else:
                print ('Que pena! Você perdeu...')
                dinheiro = dinheiro - aposta
                print ('Agora você tem R${0}'.format(dinheiro))
        elif escolha == 'i':
            if escolha%2==1:
                print ('Parabéns! Você ganhou!')
                dinheiro = dinheiro + aposta
                print ('Agora você tem R${0}'.format(dinheiro))
            else:
                print ('Que pena! Você perdeu...')
                dinheiro = dinheiro - aposta
                print ('Agora você tem R${0}'.format(dinheiro))
        else:
            print('Digite novamente alguma das opções listadas')
            
                
        