import ramdom
dado2=randint(1,6)
dado2=randint(1,6)
dado2=randint(1,6)
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
            dinheiro=dinheiro2
            while y:
                print(dinheiro2)                      
                chute=input("chute um número")
                if chute == soma:
                    final=dinheiro2+dinheiro2*5                   
                    print("Você ganhou o jogo com {0} dinheiros!".Format(final))
                    x=False
                    y=False
                else:
                    dinheiro2=dinheiro2-1
                    
                