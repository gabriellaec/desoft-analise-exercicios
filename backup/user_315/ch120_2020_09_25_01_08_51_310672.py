import random

numero = random.randint (0,36)
dinheiro = 100

print ('Bem-vindo(a) ao Jogo da Roleta!')
print ('Inicialmente, você começa com 100 dinheiros!')

while dinheiro != 0:

    dinheiro_apostado  = int(input('Digite o valor de aposta: '))

    if dinheiro_apostado == 0:

        break

    else: 
        
        tipo_de_aposta = int(input('Escolha n ou p para fazer a aposta: ')) 

        if tipo_de_aposta == 'n':
            numero_escolhido = input('Escolha um número entre 1 e 36: ')

            if numero_escolhido == numero:
                dinheiro += dinheiro_apostado*10 
                print ('Você ganhou a aposta!')
                print ('O número sorteado foi {0}'.format(numero))
                print ('Agora você tem {0} dinheiros'.format (dinheiro))

            else:
                dinheiro -= dinheiro_apostado
                print ('Você perdeu a aposta!')
                print ('O número sorteado foi {0}'.format(numero))
                print ('Agora você tem {0} dinheiros'.format (dinheiro))

        elif tipo_de_aposta == 'p':
            paridade = input('Escolha entre p ou i: ')

            if paridade == 'p':
                
                if numero%2 == 0:
                    dinheiro += dinheiro_apostado
                    print ('Você ganhou a aposta!')
                    print ('O número sorteado foi {0}'.format(numero))
                    print ('Agora você tem {0} dinheiros'.format (dinheiro))
                
                else:
                    dinheiro -= dinheiro_apostado
                    print ('Você perdeu a aposta!')
                    print ('O número sorteado foi {0}'.format(numero))
                    print ('Agora você tem {0} dinheiros'.format (dinheiro))

            elif paridade == 'i':

                if numero%2 != 0:
                    dinheiro += dinheiro_apostado
                    print ('Você ganhou a aposta!')
                    print ('O número sorteado foi {0}'.format(numero))
                    print ('Agora você tem {0} dinheiros'.format (dinheiro))
                
                else:
                    dinheiro -= dinheiro_apostado
                    print ('Você perdeu a aposta!')
                    print ('O número sorteado foi {0}'.format(numero))
                    print ('Agora você tem {0} dinheiros'.format (dinheiro))

print ('Fim de jogo')