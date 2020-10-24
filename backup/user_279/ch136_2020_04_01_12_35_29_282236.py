import random
jogo = True
dinheiros = 10
dado1 =random.randit (1,6) 
dado2 =random.randit (1,6) 
dado3 =random.randit (1,6) 
soma = dado1 + dado2 + dado3
while jogo
    print("Fase de dicas")
    print("voce tem {} dinheiros" .format(dinheiros))
    dicac= True
            while dicac
            if dinheiros > 0:
             qdica = str(input("Voce quer uma dica? custa 1 dinheiro:"))
             if qdica == "sim":
                dinheiros = dinheiros - 1
                dica1 = int(input("digite um numero:"))
                dica2 = int(input("digite outro numero:"))
                dica3 = int(input("digite outro numero:"))
                if dica1 == soma or dica2 == soma or dica3 == soma:
                    print("A soma é um desses 3 numeros")
                else:
                    print("a soma não esta entreesses 3 numeros")
             if qdica == "não"
                 dicac = False
            if dinheiros == 0
                didac = False
    chutesc = True
    while chutesc
        print("começa a fase dos chutes")
        print("voce tem {} dinheiros" .format(dinheiros))
        if dinheiros == 0:
            print("Voce perdeu!")
        elif dinheiros > 10:
            chute = int(input("Chute um numero:"))
            if chute == soma:
                dinheiros = dinheiros + dinheiros*5
                print("Você ganhou o jogo com {} dinheiros!" .format(dinheiros))
                chutesc = False
                jogo = False           
            else:
                dinheiros = dinheiros - 1