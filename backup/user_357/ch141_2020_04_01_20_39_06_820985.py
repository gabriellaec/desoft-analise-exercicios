import random

saldo = 1000
jogo = True 


while jogo == True: 
    inicio = input("Deseja realizar uma aposta? ")
    while inicio != "não":
        dado_01 = random.randint(1,6)
        dado_02 = random.randint(1,6)
        soma = dado_01+dado_02
        chute = int(input("Foram lançados dois dados de 6 lados, chute o valor da soma ao custo de 30 dinheiros: "))
        saldo -= 30
        while chute != soma:
            print("Errou!")
            novo_chute = input("Deseja 'continuar' ou 'desistir'? ")
            if novo_chute == "desistir":
                break
            else:
                chute = int(input("Foram lançados dois dados de 6 lados, chute um novo valor para a soma ao custo de 20 dinheiros: "))
                saldo -= 20
            
        if chute == soma:
            saldo += 50
            print("Parabéns vc acertou e ganhou 50 dinheiros por isso!")
            print('')
            print('Você terminou a partida com {0} dinheiros'.format(saldo))
        inicio = input("Deseja realizar uma aposta? ")
        
        
    break    