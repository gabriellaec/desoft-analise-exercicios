import random
quantidade=100
print('Sua quantidade de dinheiro inicial é R${0}'.format(int(quantidade)))
while True:
    aposta=int(input('Digite o valor de sua aposta: '))
    x=input('Digite um número ou paridade: ')
    if x=='n':
        k=int(input('Digite o numero desejado de 1 a 36: '))
        z=random.randint(0,36)
        if k==z:
            quantidade+=35*aposta
            print('Voce tem R${0}'.format(quantidade))
        else:
            quantidade=quantidade-aposta
            print('Voce tem R${0}'.format(quantidade))
    elif x=='p':
        f=input('Escolha par(p) ou ímpar(i): ')
        if f=='p':
            g=random.randint(0,36)
            if g % 2==0:
                quantidade+=aposta
                print('Voce tem R${0}'.format(quantidade))
            else:
                quantidade=quantidade-aposta
                print('Voce tem R${0}'.format(quantidade))
        if f=='i':
            g=random.randint(0,36)
            if g % 2 !=0:
                quantidade+=aposta
                print('Voce tem R${0}'.format(quantidade))
            else:
                quantidade=quantidade-aposta
                print('Voce tem R${0}'.format(quantidade))
    if aposta==0 or quantidade==0:
        break
    if aposta>quantidade:
        break                

         