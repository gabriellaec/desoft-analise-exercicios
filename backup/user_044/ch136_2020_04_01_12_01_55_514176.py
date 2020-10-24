import random
soma_dados=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
dinheiros=10
while dinheiros>=0 and dica=="não":
    print("Você tem {0} dinheiros".format(dinheiros))
    if dinheiros==0:
        print("Você perdeu!")
        dinheiros=dinheiros-1
    else:
        dica=input("Você deseja uma dica, cada dica custa um dinheiro. (sim/não)")
        if dica=="sim":
            chute1=input("Fale um número! ")
            chute2=input("Fale outro número! ")
            chute3=input("Fale outro número! ")
            dinheiros=dinheiros-1
            if chute1==soma_dados or chute2==soma_dados or chute3==soma_dados:
                print("Está entre os 3")
            else:
                print("Não está entre os 3")
        else:
            return dica        
while dinheiros>0:
    print("Você tem {0} dinheiros".format(dinheiros))
    if dinheiros==0:
        print("Você perdeu!")
    else:
        chute=input("Chute um número! ")
        if chute==soma_dados:
            dinheiros=dinheiros+dinheiros*5
            print("Você ganhou o jogo com {0} dinheiros!".format(dinheiros))
        else:
            dinheiros=dinheiros-1