import random
dinheiros = 1000
jogo = True
while jogo:
    iniciar = input('Quer apostar? (s/n): ')
    if iniciar == 'n':
        jogo = False
    else:
        dado1 = random.randint(0,6)
        dado2 = random.randint(0,6)
        sdados = dado1+dado2
        jogada = True
        valor_aposta = 30
        while jogada:
            dinheiro -= valor_aposta 
            valor_aposta -= 10
            aposta = input('Qual o valor da soma?: ')
            if aposta == sdados:
                dinheiro += 50
            else:
                if valor_aposta == 0:
                    jogada = False
                else:
                    pergunta = input('Quer continuar tentando ou vai desistir?: ')
                    if pergunta == 'desistir':
                        jogada = False
    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
    if dinheiros <= 0:
        jogo = False
                
        