from random import randint
dinheiro = 100
    while dinheiro > 0:
        print ('Você tem R${0}'.format(dinheiro))
        aposta = int(input('Quanto você quer apostar? '))
        if aposta != 0:
            escolha = str(input('Quer apostar em um número ou em uma paridade?(n / p ou i) '))
            if escolha == 'n':
                numero = int(input('Escolha um número entre 1 e 36: '))
                aleatorio = randint(0,36)
                if numero == aleatorio:
                    dinheiro = dinheiro + (aposta * 35)
                else:
                    dinheiro = dinheiro - aposta
            elif escolha == 'p':
                aleatorio = randint(0,36)
                if (aleatorio % 2 == 0):
                    dinheiro = dinheiro + aposta
                else:
                    dinheiro = dinheiro - aposta
            else:
                aleatorio = randint(0,36)
                if (aleatorio%2 != 0):
                    dinheiro = dinheiro + aposta
                else:
                    dinheiro = dinheiro - aposta
        else: 
            dinheiro = 0