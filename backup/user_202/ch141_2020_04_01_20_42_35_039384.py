import random
dinheiros = 1000
jogo = True
while jogo:
    iniciar = input('Quer apostar? (sim/não): ')
    if iniciar == 'não':
        jogo = False
    else:
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        sdados = dado1+dado2
        jogada = True
        valor_aposta = 30
        while jogada:
            dinheiros -= valor_aposta 
            valor_aposta -= 10
            aposta = int(input('Qual o valor da soma?: '))
            if aposta == sdados:
                dinheiros += 50
                jogada = False
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
                
        