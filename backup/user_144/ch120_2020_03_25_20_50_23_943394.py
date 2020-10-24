import random 
import time
dinheiro = 100
while True:

    print(f'Dinheiro atual é {dinheiro}' )
    if dinheiro == 0:
        #time.sleep(1)
        print("Acabou o dindin")
        break
    aposta = int(input("Faça uma aposta para poder jogar o game: "))
    if aposta == 0 or aposta < 0:
        print("Nao pode ser zero")
        aposta = int(input("Faça uma aposta para poder jogar o game: "))
    elif aposta > dinheiro :
        print("Aposta maior que valor atual de moedas")
        aposta = int(input("Faça uma aposta para poder jogar o game: "))
    
    pergunta = input("Deseja apostar em numero ou paridade?
Digite'n' para numero e 'p' para paridade: ")

    if pergunta == 'n':
        num = int(input("Digite entre 1 a 36: "))
        b = random.randint(0,36)
        print(f"Numero sorteado é {b}" )
        if b == num:
            dinheiro += aposta*35
        elif b != num:
            dinheiro -= aposta

    
    elif pergunta == 'p':
        par = input("Escolha entre par(p) ou ímpar(i): ")
        p = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        i = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
        b = random.randint(0,36)

        print(f"Numero sorteado é {b}" )
        if par == 'p' and b in p:
            dinheiro += aposta
        
        elif par == 'p' and b not in p:
            dinheiro -= aposta
            
        if par == 'i' and b in i:
            dinheiro += aposta
        
        elif par == 'i' and b not in i:
            dinheiro -= aposta