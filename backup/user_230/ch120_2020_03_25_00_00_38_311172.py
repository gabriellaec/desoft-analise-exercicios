from random import randint 
d=100
while (d>0):
    sorteio=randint(0,36)
    print ("Dinheiro disponível:{0}".format(d))
    a=int(input("Sua aposta:")
    b=input("A aposta é em um número (n) ou paridade(p)?")
    if a==0:
        break
    elif b=="n":
        n=int(input("Escolha um número de 1 a 36:")
        if n==sorteio:
                d=d+35*a
        else:
                 d=d-a
    else:
        pi=input("É par(p) ou ímpar(i)?")
        if pi=="i" and sorteio%2!=0:
            d=d+a
        elif pi=="p" and sorteio%2==0:
            d=d+a
        else:
            d=d-a
if d==0:
    print("Você perdeu!")