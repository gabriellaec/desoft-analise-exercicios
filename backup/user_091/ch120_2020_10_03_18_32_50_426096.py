import random
quantidade=100
print('Sua quantidade de dinheiro inicial é R${0}'.format(int(quantidade)))
while True:
    aposta=int(input('Digite o valor de sua aposta: '))
    if aposta==0 or quantidade==0:
        break
    x=input('Digite um número ou paridade: ')
    if x=='n':
        k=int(input('Digite o numero desejado de 1 a 36: '))
        z=random.randint(0,36)
        if k==z:
            quantidade+=35*aposta
        else:
            quantidade=quantidade-aposta
    elif x=='p':
        f=input('Escolha par(p) ou ímpar(i): ')
        if f=='p':
            g=random.randint(0,36)
            if g % 2==0:
                quantidade+=aposta
            else:
                quantidade=quantidade-aposta
        if f=='i':
            g=random.randint(0,36)
            if g % 2 !=0:
                quantidade+=aposta
            else:
                quantidade=quantidade-aposta
                
    print(quantidade)
         
    
    