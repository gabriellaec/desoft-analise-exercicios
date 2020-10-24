from random import randint
d1=randint(1,6)
d2=randint(1,6)
d3=randint(1,6)
d=(d1+d2+d3)
saldo=10
if saldo>0:
    fase1= True
    while fase1:
        print("fase de dicas")
        print("seu saldo é de: ",saldo,"dinheiro")
        dica=str(input("você quer uma dica?ela custa 1 dinheiro "))
        if dica in["sim","Sim"]:
            saldo= saldo - 1
            p1=int(input("digite um número"))
            p2=int(input("digite um número"))
            p3=int(input("digite um número"))
            if d in [p1,p2,p3]:
                print ("Está entre os 3")
            else:
                print("Não está entre os 3")
        else:
            fase1= False
    if saldo>0:
        fase2= True
        while fase2:
            print("fase de chutes")
            print("seu saldo é de: ",saldo,"dinheiro")
            if saldo>0:
                c=int(input("digite um número para o chute"))
                if c == d:
                    saldo=saldo*6
                    print ("Você ganhou o jogo com ",saldo," dinheiros!")
                    fase2=False
                elif c !=d:
                    print("tente novamente")
            elif saldo <=0:
                fase2=False
elif saldo <=0 :
    print("Você perdeu!")