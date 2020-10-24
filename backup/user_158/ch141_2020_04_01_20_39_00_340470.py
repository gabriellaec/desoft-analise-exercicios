import random
dinhero = 1000
custo = 30
game = True
game_start = (input("Quer jogar ?")
while game_start != "não" and game == True:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma = dado1 + dado2
    chute=int(input("qual e o seu chute ?")
    dinhero = dinhero -  custo
    print('Você terminou a partida com {0} dinheiros'.format(dinhero))
    while Chute != soma:
        game_end =input("Quer desistir ou continuar?")
        while  game_end != "desistir" and custo >= 10  :
            chute=int(input("qual e o seu chute ?")
            dinhero = dinhero - custo
            custo = custo - 10  
    print('Você terminou a partida com {0} dinheiros'.format(dinhero))
    dinhero = dinhero + 50
    game = False

                                              