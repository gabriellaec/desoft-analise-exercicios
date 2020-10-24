import random
fichas = 100

while fichas > 0:
    numero_sorteado = random.randint(1,36)
    print("Você possui {} fichas.".format(fichas))
    aposta = int(input("Quanto deseja apostar? "))
    if aposta == 0:
        break
    numero_paridade = input("Deseja apostar em um numero (n) ou em paridade(p)? ")
    if numero_paridade == 'n':
        numero = int(input('Qual o numero? '))
        if numero == numero_sorteado:
            print(numero_sorteado)
            print("Você ganhou!")
            fichas += aposta*35
        else:
            print(numero_sorteado)
            print("Você perdeu!")
            fichas -= aposta
    elif numero_paridade == 'p':
        par_impar = input("Qual a paridade: par (p) ou ímpar(i)? ")
        if numero_sorteado % 2 == 0:
            if par_impar == 'p':
                print(numero_sorteado)
                print("Você ganhou!")
                fichas += aposta
            else:
                print(numero_sorteado)
                print("Você perdeu!")
                fichas -= aposta
        else:
            if par_impar == 'i':
                print(numero_sorteado)
                print("Você ganhou!")
                fichas += aposta
            else:
                print(numero_sorteado)
                print("Você perdeu!")
                fichas -= aposta
    
