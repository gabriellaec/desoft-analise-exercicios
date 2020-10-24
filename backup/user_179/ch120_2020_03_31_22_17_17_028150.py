from random import randint
dinheiro = 100
    while dinheiro > 0:
        print ('Você tem R${0}'.format(dinheiro))
        aposta = int(input('Quanto você quer apostar? '))
        if aposta != 0:
            escolha = str(input('Quer apostar em um número ou em uma paridade?(n / p) '))
            if escolha == 'n':
                numero = int(input('Escolha um número entre 1 e 36: '))
                aleatorio = randint(0,36)
                if numero == aleatorio:
                    dinheiro = dinheiro + (aposta * 35)
                else:
                    dinheiro = dinheiro - aposta
            else:
                paridade = str(input('Você quer par ou impar? (p / i) '))
                aleatorio = randint(0,36)
                if paridade == 'p' and aleatorio % 2 == 0:
                    dinheiro = dinheiro + aposta
                elif paridade == 'i' and aleatorio%2 != 0
                    dinheiro = dinheiro + aposta
                else:
                    dinheiro = dinheiro - aposta
        else: 
            dinheiro = 0