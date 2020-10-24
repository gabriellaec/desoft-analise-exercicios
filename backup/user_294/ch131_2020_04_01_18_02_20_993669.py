import random
dinheiro=10
while dinheiro>0:
    print('Seu crédito disponível é de R${0}'.format(dinheiro))
    aposta_inicial=int(input('fale um numero:'))
    aposta_inicial2=int(input('fale outro numero: '))
    if (aposta_inicial+aposta_inicial2) <=0:
        dinheiro=0
    else:
        sort=random.randint(1,10)
        sort2=random.randint(1,10)
        if (aposta_inicial+aposta_inicial2)>(sort+sort2):
            print ('soma maior')
        elif (aposta_inicial+aposta_inicial2)<(sort+sort2):
                print ('soma menor')
        else:
            print ('soma no meio')
        print ('Seu crédito é de R${0}'.format(dinheiro))
        y=int(input('quantos chutes?: '))
        dinheiro-=y
        contador=y
        w=int(input('qual seu chute?: ')
            while w!=(sort+sort2)
                contador-=1
                w=int(input('tente de novo: ')
            if contador==0:
                dinheiro-=aposta_inicial
                print('Seu crédito é de R${0}'.format(dinheiro))

            elif w==(sort+sort2):
                dinheiro+=5*contador
                print ('Seu crédito é de R${0}'.format(dinheiro))
                