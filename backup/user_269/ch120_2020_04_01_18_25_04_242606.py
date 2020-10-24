import random
import sys

dinheiro=100
print("Voce possui {} de créditos".format(dinheiro))
valor_apostado=input("O valor a ser apostado")
if valor_apostado ==0:
    sys.exit()
else:
    Aposta=input("A aposta é em um número ou paridade?")
    numero_escolhido=int(input("Escolha seu numero de 1 a 36"))
    if Aposta=="n":
        a=random.randint(0,36)
        if numero_escolhido==a:
            dinheiro=dinheiro+35*valor_apostado
            print(dinheiro)
        else:
            dinheiro=dinheiro-valor_apostado
            print(dinheiro)
    elif Aposta=="p":
        a=random.randint(0,36)
        if numero_escolhido%2==0:
            dinheiro=dinheiro+valor_apostado
        else:
            dinheiro=dinheiro-valor_apostado
    else:
        a=random.randint(0,36)
        if numero_escolhido%2==1