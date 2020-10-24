import random

dinheiro  = 1000

while True:
    print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
    apostar = input("quer apostas?")
    if apostar == "não":
        break
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)

    print(dado1)
    print(dado2)

    dinheiro -= 30
    chute = int(input("qual é o seu chute? "))
    if chute == dado1+dado2:
        print("parabéns.")
        dinheiro += 50
        continue

    print("errou!")
    apostar = input("quer continuar tentando? ")
    if apostar == "desistir":
        continue

    dinheiro -= 20
    chute = int(input("qual é o seu novo chute? "))
    if chute == dado1+dado2:
        print("parabéns.")
        dinheiro += 50
        continue
    
    print("errou!")
    print("Um dos dados deu: {0}".format(dado1))
    apostar = input("quer continuar tentando? ")
    if apostar == "desistir":
        continue

    dinheiro -= 10
    chute = int(input("qual é o seu novo chute? "))
    if chute == dado1+dado2:
        print("parabéns.")
        dinheiro += 50
    
    continue
    