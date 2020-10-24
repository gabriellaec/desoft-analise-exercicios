import random 
import time
dinheiro = 100
while True:
    if dinheiro == 0:
        time.sleep(1)
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

    
    elif pergunta == 'p':
        par = input("Escolha entre par(p) ou ímpar(i): ")        

        
    a = random.randint(1,36)
    print(f"Numero sorteado é {a}" )
    if a == num:
        dinheiro += aposta*35
        print(f'Dinheiro atual é {dinheiro}' )
        
    elif a != num:
        dinheiro -= aposta
        print(f'Dinheiro atual é {dinheiro}' )