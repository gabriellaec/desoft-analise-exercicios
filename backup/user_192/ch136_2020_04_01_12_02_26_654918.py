import random
dinheiro = 10
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
soma = dado1 + dado2 + dado3
jogo = True
while jogo:
    print('Sua quantidade de dinheiro atual é {}').format(dinheiro)
    if dinheiro > 0:
        resposta = str(input('Quer uma dica? [s/n]')
        if resposta = 's':
            dinheiro -= 1
            numero1 = int(input('Digite o primeiro numero: '))
            numero2 = int(input('Digite o segundo numero: '))
            numero3 = int(input('Digite o terceiro numero: '))           
            if soma == numero1 or soma == numero2 or soma == numero3:
                print('A soma está entre os 3!')
            else:
                print('A soma não está entre os 3')
        else:
             print('Sua quantidade de dinheiro atual é {}').format(dinheiro)
             aposta = int(input('Digite um numero de aposta: '))
             if aposta == soma:
                 dinheiro = dinheiro + 5*dinheiro
                 print('Você ganhou o jogo com {} dinheiros!').format(dinheiro)
             else:
                 dinheiro -= 1
    else:
        jogo = False
        print('Você perdeu')
                   
    