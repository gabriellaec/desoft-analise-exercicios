from random import randint 
dinheiro=100
while (dinheiro>0):
    sorteio=randint(0,36)
    print ("Dinheiro disponível:{0}".format(dinheiro))
    aposta=int(input("Sua aposta:")
    paridade_ou_numero = input("A aposta é em um número (n) ou paridade(p)?")
    if aposta==0:
        break
    elif paridade_ou_numero=="n":
        numero=int(input("Escolha um número de 1 a 36:")
        if numero==sorteio:
                dinheiro=dinheiro+35*a
        else:
                 dinheiro=dinheiro-a
    else:
        par_ou_impar=input("É par(p) ou ímpar(i)?")
        if par_ou_impar=="i" and sorteio%2!=0:
            dinheiro=dinheiro+a
        elif par_ou_impar=="p" and sorteio%2==0:
            dinheiro=dinheiro+a
        else:
            dinheiro=dinheiro-a
if dinheiro==0:
    print("Você perdeu!")