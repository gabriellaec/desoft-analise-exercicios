import random
jogo = True
roleta = random.randit(0,36)
dinheiro = 100
while jogo:
    print ("Você tem {0} dinheiros" .format(dinheiro))
    if dinheiro <= 0:
        print("Você perdeu")
        break
    valor_aposta = int(input("Quanto você aposta: "))
    if valor_aposta <= 0:
        break
    aposta = int(input("Você aposta em um numero ou em paridade: "))
    if aposta == 'n':
        numero = int(input("escolha um numero de 1 a 36: "))
        if numero == roleta:
            dinheiro = dinheiro + 35*valor_aposta
            print ('Você acertou!')
        elif numero != roleta:
            dinheiro = dinheiro - valor_aposta
            print ("Você errou")
    elif aposta == 'p':
        numero2 = int(input("Escolha par ou impar: "))
        if numero2 == 'p' and roleta % 2 == 0:
            dinheiro = dinheiro + valor_aposta
            print ("Você acertou")
        elif numero2 == 'i' and roleta % 2 == 1:
            dinheiro = dinheiro + valor_aposta
            print ("Você acertou")
        elif numero2 == 'p' and roleta % 2 == 1:
            dinheiro = dinheiro - valor_aposta
            print ("Você errou")
        elif numero2 == 'i' and roleta % 2 == 0:
            dinheiro = dinheiro - valor_aposta
            print ("Você errou")
    roleta = random.randit(0,36)
            