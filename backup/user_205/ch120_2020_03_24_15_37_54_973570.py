from random import randint 
dinheiro = 100
while (dinheiro != 0 and dinheiro > 0):
    sorteio = randint(0,36)
    print ("Olá! Você está com {0} fichas".format(dinheiro)) 
    aposta = int(input("Aposte um valor para a rodada: "))
    paridade_ou_numero = input("A aposta é em paridade ou numero (p/n): ")
    if aposta == 0:
        break
    elif  paridade_ou_numero == "n":
        numero = int(input("Digite um numero de 1 a 36: "))
        if numero == sorteio:
            dinheiro = dinheiro + 35*aposta
        else:
            dinheiro = dinheiro - aposta
    else:  
        paridade = input("É par ou impar (p/i): ")
        if paridade == "i" and sorteio % 2 !=0:
            dinheiro = dinheiro + aposta
        else:
            dinheiro = dinheiro - aposta         
if dinheiro == 0: 
    print ("Você perdeu! Las Vegas não é para você!")
    print (sorteio)
            
        
