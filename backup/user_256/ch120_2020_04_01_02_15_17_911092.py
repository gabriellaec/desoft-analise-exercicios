import random
print("Voce tem 100 dinheiros ")
inicial =100
dinheiro = inicial
aposta = True
while aposta>0 and dinheiro>0:
    perg=input("Numero ou paridade? ")
    if perg== "n":
        aposta = int(input("quanto deseja apostar? "))
        digita=int(input("Digita um numero entre 1 e 36: "))
        sorteio1 = random.randint(0, 36)
        if sorteio1==digita:
            dinheiro = dinheiro+(aposta*35)
        else:
            dinheiro = dinheiro-aposta
        print("Agora voce tem {0}".format(dinheiro))  
    if perg == "p":
        aposta = int(input("quanto deseja apostar? "))
        sorteio2 = random.randint(0, 36)
        digita=input("par digite p, impar digite i")
        if digita == "p" and sorteio2 %2 == 0:
            dinheiro = dinheiro + aposta
        if digita == "p" and sorteio2 %2 == 1:
            dinheiro = dinheiro - aposta
        if digita == "i" and sorteio2 %2 == 1:
            dinheiro = dinheiro + aposta
        if digita == "i" and sorteio2 %2 == 0:
            dinheiro = dinheiro - aposta
            
        print("Agora voce tem {0}".format(dinheiro))
if dinheiro<=0:
    aposta = False
    print("GAME OVER parceiro")