from random import randint
dado1 = randint(1,10)
dado2 = randint(1,10)
soma_dados = dado1 + dado2
dinheiro = 10
dicas = True
chutes = True
jogo = True 
while jogo:
    while dicas:
        numero1 = int(input('Escolha um número: '))
        numero2 = int(input('Escolha um número maior ou igual ao número escolhido anteriormente: ')
        if soma_dados < numero1:
            print('"Soma menor"')
        elif soma_dados > numero2:
            print('"Soma maior"')
        else:
            print('"Soma no meio"')
        dicas = False
    while chutes:
        print('Você possui {0} dinheiros disponível'.format(dinheiro))
        compra = int(input('Cada chute custa 1 dinheiro, quantos chutes você quer comprar?: ')
        dinheiro = dinheiro - compra
        while compra > 0 and dinheiro > 0:
            aposta = int(input('Escolha um número para apostar: ')
            if aposta == soma_dados:
                dinheiro = dinheiro + 5*dinheiro
                jogo = False
            else:
                chutes = True
        if dinheiro == 0:
            jogo = False
if jogo = False:
    print('"Você terminou o jogo com {0} dinheiros"'.format(dinheiro)               