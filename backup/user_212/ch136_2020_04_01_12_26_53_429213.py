from random import randint

dado1=(randint (0,36))
dado2=(randint (0,36))
dado3=(randint (0,36))
dados=dado1 + dado2+ dado3
dinheiros=10
dica=0
chute=0

#fase de dicas

while(dica!='não'):    
    resposta_perdeu= ("Você perdeu!")
    print(dinheiros)
    if dinheiros == 0:
        print (resposta_perdeu)
    else:
        dica=("você quer uma dica?")
        if dica == "sim":
            n1=input("digite um número")
            n2=input("digite um número")
            n3=input("digite um número")
            if n1 == dados or n2==dados or n3==dados :
                print ("Está entre os 3")
            else:
                print("Não está entre os 3")
            dinheiros -=1
#fase chutes:
            
while(chute != dados):
    resposta_ganhou=("você ganhou com [0]" .format (dinheiros))
    resposta_perdeu= ("Você perdeu!")   
    print(dinheiros)
    if dinheiros == 0:
        print (resposta_perdeu)
    else:
        chute=input("Chute um número")
        if chute != dados:
            dinheiros -=1
        else:
            dinheiros += dinheiros*5
            print (resposta_ganhou)