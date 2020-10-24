import random

dinheiro=100
while dinheiro>0:
    print('*****')
    print(dinheiro)
    valor_aposta=float(input('aposta: '))
    if valor_aposta==0:
        break
    else:
        numero_sorte=random.randint(1,36)
        tipo_aposta=input('a aposta será número(n) ou paridade(p)? ')
        if tipo_aposta=='n':
            print('ecolheu número, agora:')
            numero_apostado=int(input('um número de 1 a 36: '))
            if numero_apostado==numero_sorte:
                dinheiro+=35*valor_aposta
            else:
                dinheiro-=valor_aposta
        elif tipo_aposta=='p':
            print('escolheu paridade, agora')
            paridade=input('a aposta é em par(p) ou em impar(i): ')
            if paridade=='p' and numero_sorte%2==0:
                dinheiro+=valor_aposta
                print('acertou, é par')
            elif paridade=='i' and numero_sorte%2==0:
                dinheiro-=valor_aposta
                print('errou, é par')
            elif paridade=='i' and numero_sorte%2!=0:
                dinheiro+=valor_aposta
                print('acertou, é ímpar')
            else:
                dinheiro-=valor_aposta
                print('errou, é ímpar')
        else:
            break