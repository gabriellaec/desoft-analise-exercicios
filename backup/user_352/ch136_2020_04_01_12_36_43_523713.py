import ramdom
dado2=ramdom.randint(1,6)
dado2=ramdom.randint(1,6)
dado3=ramdom.randint(1,6)
soma=dado1+dado2+dado3
dinheiro=10
x=True
y=True
while x:
    print(dinheiro)
    if dinheiro == 0:
        x=False 
        print("Você perdeu!")
    else:
        dica=input("Quer uma dica?")
        if dica == "sim":
            dinheiro=dinheiro-1
            primeiro=input("escolha o primeiro número")
            segundo=input("escolha o segundo número")
            terceiro=input("escolha o terceiro número")
            if soma == primeiro or soma == segundo or soma == terceiro:
                print("Está entre os 3")
            else:
                print("Não está entre os 3")
        else:
            while y:
                print(dinheiro)                      
                chute=input("chute um número")
                if chute == soma:
                    final=dinheiro+dinheiro*5                   
                    print("Você ganhou o jogo com {0} dinheiros!".Format(final))
                    x=False
                    y=False
                else:
                    dinheiro=dinheiro-1
                    
                