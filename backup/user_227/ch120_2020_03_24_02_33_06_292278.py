import random

dinheiro = 100

while not dinheiro <= 0:
    
    print("Você tem {0} dinheiros".format(dinheiro))
    valor = float(input("Você aposta quanto? "))
    if valor == 0:
            break
    aposta = input("A aposta é em número (n) ou em paridade (p)? ")
    if aposta == "n":
        numero = random.randint(0, 36)
       
        chute = int(input("Digite um número de 1 a 36: "))
        
        if chute == numero:
            dinheiro = (dinheiro - valor) + valor * 35
            
        else: 
            dinheiro = dinheiro - valor
            
    else:
        numero = random.randint(0, 36)
       
        par_ou_impar = input("Par (p) ou ímpar (i)? ")
        
        if par_ou_impar == "p":
            
            if numero % 2 == 0:
                dinheiro = dinheiro + valor
                
            else:
                dinheiro = dinheiro - valor
               
        
        else:
            
            if numero % 2 != 0:
                dinheiro = dinheiro + valor
                
            else:
                dinheiro = dinheiro - valor