from random import randint 

def dados():
    dad1 = randint(1,6)
    dad2 = randint(1,6)
    dad3 = randint(1,6)
    return dad1 + dad2 + dad3
    
dinheiro = 10
d = dados()
while dinheiro > 0:
    print("Você tem {} moedas".format(dinheiro))
    dica = input("Você quer uma dica?(sim/não)(custo = 1 moeda) ")
    
    if dica == "sim":
        prim = int(input("Escolha um número de 1 a 18: "))
        segu = int(input("Escolha outro diferente de 1 a 18: "))
        terc = int(input("Escolha outro diferente de 1 a 18: "))
        if prim == d or segu == d or terc == d:
            print("Está entre os 3")
            dinheiro-=1
        else:
            print("Não está entre os 3")
            dinheiro-=1
    else:
        while dinheiro > 0:
            print("Você tem {} moedas".format(dinheiro))
            chute = int(input("Chute um número de 1 a 18: "))
            if chute == d:
                dinheiro += dinheiro*5
                print("Você ganhou o jogo com {} dinheiros!".format(dinheiro))
                break
            else:
                dinheiro-=1
        break
                
else:
    print("Você perdeu!")
    
