import random
dinheiro = 100
print('Seu dinheiro é ',dinheiro )
while dinheiro > 0:
    a = random.randint(0,36)
    aposta = int(input('Digite o valor de sua aposta'))
    if aposta==0:
        dinheiro = 0
    aposta_1 = input('Escolha entre as seguintes opções n,i,p')
    dinheiro -=aposta
    print('Seu dinheiro depois da aposta é',dinheiro)
    if aposta_1 == 'n':
        numero136 = int(input('Digite um numero de 1 a 36'))
        if numero136 ==a:
            dinheiro = dinheiro+(35*aposta) 
            print('Seu saldo é de ',dinheiro)
        else:
            print('Seu saldo é de ',dinheiro)   
    if aposta_1 == 'i':
        if a % 2 != 0:
            dinheiro +=aposta*2
            print('Seu saldo é de ',dinheiro)   
        else: 
            print('Seu saldo é de ',dinheiro) 
    if aposta_1 == 'p':
        if a%2 == 0:
            dinheiro +=aposta*2
            print('Seu saldo é de ',dinheiro)   
        else:
            print('Seu saldo é de ',dinheiro)     
