import random
perg=input("Você quer apostar(s/n)")
while perg!="n":
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    soma=dado1+dado2
    dininicial=1000
    print(f"Voce tem {dininicial} dinheiros disponíveis")
    aposta=30
    print(f"O valor da aposta é {aposta}")
    chute=input("Número chutado: ")
    if chute == soma:
        din=dininicial-aposta+30
    else:
        d=input("Quer continuar ou sair(c/s)")
        if d=="s":