import random
dinheiro= 100   #sempre mostrar o dinheiro disponível  

while dinheiro > 0:
    roleta = random.randint(0,36)
    print (dinheiro)
    aposta = float(input("Que valor deseja apostar?: "))
    
    if aposta <=0:
        break  
    
    qual_aposta= input("A aposta é número ou paridade? n/p: ")
    
    if qual_aposta =="n":
        digite = int(input("Digite um valor entre 0 e 36: "))
        if digite==roleta:
            dinheiro+= aposta * 35
        else:
            dinheiro -= aposta
    
    elif qual_aposta =="p":
        par_ou_impar= input("Par ou ímpar? p/i: ")
        if roleta%2==0:
            resp = 'p'
        else:
            resp = 'i'
            
        if par_ou_impar==resp:
            dinheiro += aposta
        else:
            dinheiro -= aposta