import random

dinheiro = 100
print(dinheiro)

while dinheiro > 0:
    print('Digite sua aposta:')
    valor_aposta = int(input())
    print('')
    roleta = random.randint(1, 36)

    if valor_aposta == 0:
        dinheiro = 0 # Programa para de funcionar
    else:
        print('Sua escolha é um número (digite n) ou paridade (par: p/ímpar: i)?')
        tipo_aposta = (input())
        print('')

        if tipo_aposta == 'n':
            print('Você escolheu número. Digite um número entre 1 e 36:')
            escolha1 = int(input())
            print('')

            if escolha1 == roleta:
                dinheiro = 35*valor_aposta + dinheiro
                print('Agora você tem R$ {0}'.format(dinheiro))
            else:
                dinheiro = dinheiro - valor_aposta
                print('Agora você tem R$ {0}'.format(dinheiro))
        
        elif tipo_aposta == 'p':
            print('Escolha par (p) ou ímpar(i)')
            escolha1 = input()
            print('')

            if escolha1 == 'p' and roleta %2 == 0:
                dinheiro = dinheiro + valor_aposta
                print('Agora você tem R$ {0}'.format(dinheiro))
            elif escolha1 == 'p' and roleta %2 != 0:
                dinheiro = dinheiro - valor_aposta
                print('Agora você tem R$ {0}'.format(dinheiro))
            elif escolha1 == 'i' and roleta %2 == 0:
                dinheiro = dinheiro - valor_aposta
                print('Agora você tem R$ {0}'.format(dinheiro))
            elif escolha1 == 'p' and roleta %2 != 0:
                dinheiro = dinheiro + valor_aposta
                print('Agora você tem R$ {0}'.format(dinheiro))
    print('-----------------------------------------------------------------')
    print('Vamos mais uma vez')