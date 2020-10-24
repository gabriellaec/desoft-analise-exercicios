import random

money = 100

while money > 0:
    print("din={0}" .format(money)
    aposta_inicial = int(input("Quanto quer apostar? "))
    if aposta_inicial <= 0:
        money = 0
    else:
        escolha_tipo = input("Digite o tipo da aposta:")   
        if escolha_tipo == 'n':
            numero = int(input('Número de 1 a 36:'))
            if numero == random.randint(0,36):
                money += 35*aposta_inicial
                print(money)
            else:
                money -=aposta_inicial
                print(money)
        elif escolha_tipo == 'p':
            escolha_tipo2 = input("Digite o tipo da aposta:")  
            if escolha_tipo2 == 'p':
                if random.randint(0,36) % 2 == 0:
                    money += aposta_inicial
                    print(money)
                else:
                    money -= aposta_inicial
                    print(money)
            elif escolha_tipo2 == 'i':
                if random.randint(0,36) % 2 != 0:
                    money += aposta_inicial
                    print(money)
                else:
                    money -= aposta_inicial
                    print(money)