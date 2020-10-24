import random

soma_gerada = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

dinheiro = 10

def fase_dicas(din):
    while True:
        print(din)

        if din <= 0:
            perdeu = True
            return din, perdeu 
        
        resp = input("Você quer uma dica? ")

        if resp == "sim":
            din -= 1

            soma1 = int(input("Digite a primeira soma: "))
            soma2 = int(input("Digite a segunda soma: "))
            soma3 = int(input("Digite a terceira soma: "))
            
            if soma_gerada in [soma1, soma2, soma3]:
                print("Está entre os 3")
            else:
                print("Não está entre os 3")
        else:
            return din, False


def fase_chutes(din, perdeu):
    if perdeu:
        return din, False
    
    while True:
        print(din)

        if din <= 0:
            return din, False

        chute = int(input("Chute um número: "))

        if chute == soma_gerada:
            din += din*5
            return din, True
        
        din -= 1


dinheiro, perdeu = fase_dicas(dinheiro)
dinheiro, ganhou = fase_chutes(dinheiro, perdeu)

if ganhou:
    print(f"Você ganhou o jogo com {dinheiro} dinheiros!")
else:
    print("Você perdeu!")