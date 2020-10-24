dinheiro = 10
import random
soma_gerada = random.randint(0,18)
# FASE DE DICAS
while dinheiro > 0:
    print('Você tem R${0}'.format(dinheiro))
    if dinheiro <= 0:
        print('Você perdeu!')
        break
    else:
        dica = input('Você quer uma dica?(sim/não) ')
        if dica == 'sim':
            dinheiro = dinheiro - 1
            n1 = int(input('Soma chute 1: '))
            n2 = int(input('Soma chute 2: '))
            n3 = int(input('Soma chute 3: '))
            if soma_gerada == n1 or soma_gerada == n2 or soma_gerada == n3:
                print('Está entre os 3')
            else:
                print('Não está entre os 3')
                
# FASE DE CHUTES
        else:
            while dinheiro > 0:
                print('Você tem R${0}'.format(dinheiro))
                chute = int(input('Chute um número: '))
                if chute == soma_gerada:
                    dinheiro = dinheiro * 5
                    print('Você ganhou o jogo com {0} dinheiros!'.format(dinheiro))
                    break
                else:
                    dinheiro = dinheiro - 1
                    if dinheiro > 0:
                        print('Tente outro!')
                    else: 
                        print('Você perdeu!')
                        break
            break
