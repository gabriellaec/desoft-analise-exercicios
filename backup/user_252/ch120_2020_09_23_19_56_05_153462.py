import random
numero=random.randint(1, 36)
dinheiro = 100
while dinheiro!=0:
    print(dinheiro)
    dinheiro_apostado=int(input('Valor da aposta: '))

    if dinheiro_apostado==0:
        break

    else:
        tipo_aposta = input('Escolha "n" ou "p" para fazer a aposta: ')
        
        if tipo_aposta == 'n':
            numero_escolhido=input('Escolha um numero entre 1 a 36: ')
            if numero_escolhido == numero:
                dinheiro = dinheiro + (dinheiro_apostado*35)
                print('O número sorteado: {0}'.format(numero))
                print('Você ganhou a aposta')
            else:
                dinheiro-=dinheiro_apostado
                print('O número sorteado: {0}'.format(numero))
                print('Vc perdeu a aposta')
        
        elif tipo_aposta == 'p':
            paridade=input('Escolha entre p ou i: ')

            if paridade=='p':
                if numero%2==0:
                    dinheiro+=dinheiro_apostado
                    print('O número sorteado: {0}'.format(numero))
                    print('Voce ganhou a aposta')
                else:
                    dinheiro-=dinheiro_apostado
                    print('O número sorteado: {0}'.format(numero))
                    print('Voce perdeu a aposta')

            elif paridade=='i':
                if numero%2!=0:
                    dinheiro+=dinheiro_apostado
                    print('O número sorteado: {0}'.format(numero))
                    print('Voce ganhou a aposta')
                else:
                    dinheiro-=dinheiro_apostado
                    print('O número sorteado: {0}'.format(numero))
                    print('Voce perdeu a aposta')
                    
print('fim de jogo')

