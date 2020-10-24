from random import randint
dinheiro=10
fase="dica"
d1=randint(1,6)
d2=randint(1,6)
d3=randint(1,6)
soma=d1+d2+d3
while dinheiro>0:
    if fase=="dica":
        print("voce tem {0} dinheiros".format(dinheiro))
        ajuda=input("voce quer uma dica? ")
        if ajuda=="sim":
            dinheiro-=1
            op1=int(input("degite a primeira opcao"))
            op2=int(input("degite a segunda opcao"))
            op3=int(input("degite a terceira opcao"))
            if soma==op1 or soma==op2 or soma==op3:
                print("Está entre os 3")
            else:
                print("Não está entre os 3")
        elif ajuda=="não":
            fase="chute"
    elif fase=="chute":
        print("voce tem {0} dinheiros".format(dinheiro))
        ch=int(input("qual seu chute?"))
        if ch==soma:
            dinheiro*=5
            print("Você ganhou o jogo com {0} dinheiros!".format(dinheiro))
            break
        elif ch != soma:
            dinheiro-=1
print("Você perdeu!")
