import random
x= random.randint (0, 36)
usuario=100
while usuario>0:
    aposta= input("Quanto deseja apostar?: ")
    if aposta=="0":
        break
    elif aposta>usuario or aposta<0:
        print("Valor inválido, tente novamente")
        return aposta
    else:
        perg= input("Sua aposta é um número(n), ou paridade(p)?: ")
            
        if perg=="n":
            perg2= input("Digite um número de 1 a 36: ")
            if perg2==x:
                print("Você ganhou!!")
                usuario += aposta*35
            else:
                print("Você perdeu :/")
                usuario -= aposta
            
        elif perg2=="p":
            perg3= input("Par(p) ou impar(i)?: ")
            
            