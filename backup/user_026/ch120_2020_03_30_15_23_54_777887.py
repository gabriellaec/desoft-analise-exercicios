import random
dinheiro=100
while dinheiro>0:
    print(dinheiro)
    aposta = int(input("Qual valor deseja apostar? ")
    paridade = input("Sua aposta é um numero par?(n/p) ")
    if paridade =="n":
    	numero= int(input("digite um número de 1 a 36: ")
        numero_aleatorio= random.randint(1,36)
        if numero==numero_aleatorio:
            dinheiro+=aposta*35
        else:
            dinheiro-=aposta
    else:
        par_impar= input("escolha se o número será par ou ímpar (p/i): ")
        numero_aleatorio= random.randint(1,36)
        if par_impar=="p":
            if numero_aleatorio%2=0:
                dinheiro+=aposta
            else:
                dinheiro-=aposta
        else:
            if numero_aleatorio%2=0:
                dinheiro-=aposta
            else:
                dinheiro+=aposta
