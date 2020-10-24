def lista_primos(numero):
    if numero==1:
        print('Inválido')
    if numero==2:
        print(2)
    else:
        i=0
        while numero>2:
            if numero % 2==0:
                break
            else:
                soma=0
                x=3
                if numero % x==0:
                    break
                soma+=numero
                x+=2
    
    
    