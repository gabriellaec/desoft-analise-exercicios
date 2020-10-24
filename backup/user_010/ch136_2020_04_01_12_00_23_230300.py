import random


dinheiro=10
dicas=True
jogo=True
chutes=True
while jogo:
    dado1=random.randint (1,6)
    dado2=random.randint (1,6)
    dado3=random.randint (1,6)
    soma=dado1+dado2+dado3
    
    
    while dicas:
        print ("Fase de dicas")
        print ("Você tem {} dinheiros.".format (dinheiro))
        
        if dinheiro==0:
            jogo=False
            print ("Você perdeu o jogo!")
            
        else:
            pergunta=str(input("Você quer uma dica?"))
            
            if pergunta=="sim":
                dinheiro=dinheiro-1
                dica1=int(input("Digite o primeiro número:  "))
                dica2=int(input("Digite o segundo número:  "))
                dica3=int(input("Digite o terceiro número:  "))
                
                if dica1==soma or dica2==soma or dica3==soma:
                    print ("Está entre os três.")
                    
                else:
                    print ("Não está entre os três.")
                    
            elif pergunta=="não":
                dicas=False
        
    while chutes:
        print ("Fase de chutes")
        print ("Você tem {} dinheiros.".format (dinheiro))
        if dinheiro==0:
            jogo=False
            print ("Você perdeu o jogo!")
        
        else:
            chute=int(input("Chute um número:  "))
            if chute==soma:
                dinheiro=dinheiro + 5*dinheiro
                print ("Você acertou!")
                chutes=False
                jogo=False
                print ("Você ganhou o jogo com {} dinheiros.".format (dinheiro))
            else:
                print ("Você errou!")
                dinheiro=dinheiro-1
                if dinheiro==0:
                    print ("Você perdeu!")
                    chutes=False
                    jogo=False