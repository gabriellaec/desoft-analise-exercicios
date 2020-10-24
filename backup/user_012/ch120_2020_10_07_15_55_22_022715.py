import random 
i=100
while True:
    print(f' A sua quantidade de dinheiro é R${i}')
    ap=int(input('Qual sua aposta: '))
    valor=input('Vai em número(n) ou paridade(p): ')
    if valor=='n':
        d=int(input('Digite o número de 1 a 36: '))
        c=random.randint(0,36)
        if d==c:
              i=i+ap*35
              print('Voce tem R${0}'.format(i))
        else:
              i=i-ap
              print('Voce tem R${0}'.format(i))
              
    elif valor=='p':
         
        h=input('Par(p) ou ímpar(i): ')
        if h=='p':
            r=random.randint(0,36)
            if r % 2==0:
                i=i+ap
                print('Voce tem R${0}'.format(i))
            else:
                i=i-ap
                print('Voce tem R${0}'.format(i))
        elif h=='i':
            t=random.randint(0,36)
            if t % 2!=0:
                i=i+ap
                print('Voce tem R${0}'.format(i))
            else:
                i=i-ap
                print('Voce tem R${0}'.format(i))
    if i==0 or ap>i:
        break