from random import randint 
sorteio = randint(0,36)
dinheiro = 100
print ("Olá! Você está com {0} fichas".format(dinheiro))
while (dinheiro != 0 and dinheiro < 0): 
    aposta = int(input("Aposte um valor para a rodada: "))
    paridade_ou_numero = input("A aposta é em paridade ou numero: ")
    if aposta == 0:
        break
    elif  paridade_ou_numero == "numero":
        numero = int(input("Digite um numero de 1 a 36: "))
        if numero == sorteio:
            dinheiro = dinheiro + 35*aposta
            print ("Olá! Você está com {0} fichas".format(dinheiro))
        else:
            dinheiro = dinheiro - aposta
            print ("Olá! Você está com {0} fichas".format(dinheiro))
    elif  paridade_ou_numero == "paridade":
        paridade = input("É par ou impar: ")
        if paridade == "par" and sorteio % 2 ==0:
            dinheiro = dinheiro + aposta
            print ("Olá! Você está com {0} fichas".format(dinheiro))
        else:
            dinheiro = dinheiro - aposta
            print ("Olá! Você está com {0} fichas".format(dinheiro))
        
