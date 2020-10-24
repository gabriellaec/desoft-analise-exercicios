import random
dinheiro = 100
while dinheiro > 0:
    print(f"Voce tem {dinheiro} dinheiros")
    aposta = int(input("Quanto voce quer apostar? "))
    if aposta == 0:
        dinheiro = 0 #zera e para de jogar
    opcao = input("Escolha entre numero('n') ou par ou impar('p')")
    if opcao == 'n':
        escolhido = int(input('Escolha um numero de 1 a 36: '))
        sorteado = random.randint(1,36)
        if escolhido == sorteado:
            dinheiro = dinheiro + aposta*35  #ganha
        if escolhido != sorteado:
            dinheiro = dinheiro - aposta #perde
    if opcao == 'p':
        escolha_pi = input("Escolha entre par('p') ou impar('i')")
        sorteado = random.randint(1,36)
        if escolha_pi == 'p':   #escolheu par
            if sorteado % 2 == 0:
                dinheiro = dinheiro + aposta #ganha
            if sorteado % 2 != 0:
                dinheiro = dinheiro - aposta #perde
        if escolha_pi == 'i':   #escolheu impar
            if sorteado % 2 != 0:
                dinheiro = dinheiro + aposta #ganha
            if sorteado % 2 == 0:
                dinheiro = dinheiro - aposta #perde