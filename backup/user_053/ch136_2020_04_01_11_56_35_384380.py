# Joguinho da sorte para perder dinheiro :)

dado_1 = 5
dado_2 = 1
dado_3 = 6
soma_dos_dados = dado_1 + dado_2 + dado_3

dinheiro = 10
jogo_valendo = True
fase_de_dicas = True
fase_de_chutes = True

while jogo_valendo:

    if dinheiro == 0:
        print('Você perdeu!')
        jogo_valendo = False
    else:       
        while fase_de_dicas:
            print('Dinheiro disponível: R$ {0}'.format(dinheiro))
            print('')

            if dinheiro == 0:
                print('Você perdeu!')
                fase_de_dicas = False
                jogo_valendo = False
                print('')
            elif dinheiro >= 1:                         # Valores inteiros para dinheiro, nesse jogo
                print('Você quer uma dica? Responda sim ou não')
                resposta1 = input()
                print('')

                if resposta1 == 'sim':
                    dinheiro -= 1   # preço da dica
                    print('Escolha 3 números:')
                    numero_1 = int(input('Digite o primeiro número: '))
                    numero_2 = int(input('Digite o segundo número: '))
                    numero_3 = int(input('Digite o terceiro número: '))
                    print('')

                    if numero_1 == soma_dos_dados or numero_2 == soma_dos_dados or numero_3 == soma_dos_dados:
                        print('Está entre os 3')
                        fase_de_dicas = True
                        print('')
                    else:
                        print('Não está entre os 3')
                        print('')
                        fase_de_dicas = False
        
        while fase_de_chutes:
            print('Dinheiro disponível: R$ {0}'.format(dinheiro))
            print('')

            if dinheiro == 0:
                print('Você perdeu!')
                fase_de_chutes = False
                jogo_valendo = False
            elif dinheiro >= 1:                         # Valores inteiros para dinheiro, nesse jogo
                chute = int(input('Dê um chute: '))
                print('')

                if chute == soma_dos_dados:
                    dinheiro = dinheiro + 5*dinheiro
                    fase_de_chutes = False
                    jogo_valendo = False
                    print('Você ganhou o jogo com {0} dinheiros!'.format(dinheiro))
                else:
                    dinheiro -= 1
