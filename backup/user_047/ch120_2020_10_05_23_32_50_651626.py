import random
dinheiro = 100
while dinheiro > 0:
    a = random.randint(1,36)
    print(a)
    aposta = int(input('Digite o valor de sua aposta'))
    aposta_1 = input('Escolha entre as seguintes opções n,i,p')
    if aposta_1 == 'n':
        numero136 = int(input('Digite um numero de 1 a 36'))
        if numero136 ==a:
            dinheiro = dinheiro+(35*aposta) 
            print(dinheiro)
        else:
            dinheiro = dinheiro-aposta
            print(dinheiro)   
    if aposta_1 == 'i':
        if a % 2 != 0:
            dinheiro +=aposta
            print(dinheiro)   
        else:
            dinheiro = dinheiro-aposta  
            print(dinheiro) 
    if aposta_1 == 'p':
        if a%2 == 0:
            dinheiro +=aposta
            print(dinheiro)   
        else:
            dinheiro = dinheiro-aposta  
            print(dinheiro)            

