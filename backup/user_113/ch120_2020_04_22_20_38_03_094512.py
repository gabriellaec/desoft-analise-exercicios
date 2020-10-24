import random
dinheiro = 100
while dinheiro>0:
    print(dinheiro)
    aposta=float(input("Quanto deseja apostar?: "))
    while aposta<=0 or aposta>dinheiro:
        aposta=float(input("Quanto deseja apostar?: "))
    if aposta=="0":
        break
        
    perg= input("Numero(n) ou paridade(p): ")
    if perg=="n":
        valor=int(input("Escolha entre 1 e 36: "))
        x= random.randint(0, 36)
        if valor==x:
            dinheiro+=aposta*35
        else:
            dinheiro-=aposta
            
    elif perg=="p":
        perg2= input("Par(p) ou impar(i): ")
        p_ou_i= x%2
        if p_ou_i==0:
            r = "p"   
        else:
            r = "i"
        if perg2==r:
            dinheiro += aposta
        else:
            dinheiro -= aposta