import random as rnd

def dicas(soma):
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    num3 = int(input('Terceiro número: '))
    nums = [num1, num2, num3]

    if soma in nums:
        return("Está entre os 3")
    else:
        return("Não está entre os 3")

dado1 = rnd.randint(1,6)
dado2 = rnd.randint(1,6)
dado3 = rnd.randint(1,6)

soma = dado1 + dado2 + dado3
dinheiro = 10
fase_dicas = True

while fase_dicas:
    print(f'Você possui {dinheiro} dinheiros')
    if dinheiro <= 0:
        break

    quer_dica = input('Você quer uma dica? (cada dica custa 1 dinheiro) (sim/não)')
    if quer_dica == 'sim':
        print(dicas(soma))
        dinheiro-=1

    elif quer_dica == 'não':
        fase_dicas = False

while not fase_dicas:
    print(f'Você possui {dinheiro} dinheiros')
    if dinheiro <= 0:
        break

    else:
        chute = int(input('Chute um número: '))
        if chute == soma:
            dinheiro*=6
            break
        else:
            dinheiro-=1

if dinheiro > 0:
    print(f"Você ganhou o jogo com {dinheiro} dinheiros!")

else:
    print("Você perdeu!")