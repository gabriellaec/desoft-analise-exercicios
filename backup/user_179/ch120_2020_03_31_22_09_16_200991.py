from random import randint
dinheiro = 100
    while dinheiro > 0:
        print ('Você tem R${0}'.format(dinheiro))
        aposta = int(input('Quanto você quer apostar? '))
        if aposta != 0:
            escolha = str(input('Quer apostar em um número ou em uma paridade?(n / p ou i) '))
            aleatorio = randint(1,36)
            if escolha == 'n':
                numero = int(input('Escolha um número entre 1 e 36: '))
                if numero == aleatorio:
                    print ('Parabéns! Você ganhou!')
                    dinheiro = dinheiro + (aposta * 35)
                else:
                    print ('Que pena! Você perdeu...')
                    dinheiro = dinheiro - aposta
            elif escolha == 'p':
                if (aleatorio % 2 == 0):
                    print ('Parabéns! Você ganhou!')
                    dinheiro = dinheiro + aposta
                else:
                    print ('Que pena! Você perdeu...')
                    dinheiro = dinheiro - aposta
            else:
                if (aleatorio%2 != 0):
                    print ('Parabéns! Você ganhou!')
                    dinheiro = dinheiro + aposta
                else:
                    print ('Que pena! Você perdeu...')
                    dinheiro = dinheiro - aposta
        else: 
            dinheiro = 0