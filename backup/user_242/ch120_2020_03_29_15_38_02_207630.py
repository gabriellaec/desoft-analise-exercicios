import random
dinheiros = 100
while dinheiros != 0:
    print('Você tem {0} dinheiros'.format(dinheiros))
    aposta = int(input('Qual o valor da aposta?'))
    if aposta != 0:
        numero_ou_paridade = input('Sua aposta é um numero ou uma paridade? (Digite n ou p)' )
        if numero_ou_paridade == 'n':
            Roleta = random.randint(1,36)
            if Roleta ==  aposta:
                print('Você ganhou!')
                dinheiros = dinheiros + aposta * 35
            else:
                print('Você perdeu!')
                dinheiros = dinheiros - aposta

        elif numero_ou_paridade == 'p':
            Roleta = random.randint(1,36)
            par_ou_impar = input('Você escolhe par ou impar? (digite par ou impar)')
            if par_ou_impar == 'par':
                if Roleta == aposta:
                    dinheiros = dinheiros + aposta
                else:
                    dinheiros = dinheiros - aposta

            elif par_ou_impar == 'impar':
                if Roleta == aposta:
                    dinheiros = dinheiros + aposta
                else:
                    dinheiros = dinheiros - aposta

    else:
        break
print ('jogo encerrado')