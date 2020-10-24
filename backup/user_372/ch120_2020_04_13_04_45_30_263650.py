import math
import random
#Jogo de roleta
dinheiro=100
while dinheiro>0:
    valor=int(input('Quanto você deseja apostar? '))
    opcao=str(input('Digite a opção de aposta que deseja realizar: '))
#Opção número:
    if opcao=='n':
        numero_escolhido=int(input('Em qual número você deseja apostar? '))
        numero_sorteado=random.randint(1,36)
        if numero_escolhido==numero_sorteado:
            dinheiro+=valor*35
            print('Parabéns, você acertou!')
            print('Você possui agora {0}.'.format(dinheiro))
        else:
            dinheiro-=valor
            print('Você perdeu.')
            print('Você possui agora {0}.'.format(dinheiro))
#Opção par ou ímpar:   
    if opcao=='p':
        par_impar=str(input('Você escolhe par(p) ou ímpar(i)? '))
        if par_impar=='p':
            numero_sorteado=random.randint(1,36)
            if numero_sorteado%2==0:
                dinheiro+=valor
                print('Parabéns, você acertou!')
                print('Você possui agora {0}.'.format(dinheiro))
            else:
                dinheiro-=valor
                print('Você perdeu.')
                print('Você possui agora {0}.'.format(dinheiro))
        if par_impar=='i':
            numero_sorteado=random.randint(1,36)
            if numero_sorteado%2!=0:
                dinheiro+=valor
                print('Parabéns, você acertou!')
                print('Você possui agora {0}.'.format(dinheiro))
            else:
                dinheiro-=valor
                print('Você perdeu.')
                print('Você possui agora {0}.'.format(dinheiro))
