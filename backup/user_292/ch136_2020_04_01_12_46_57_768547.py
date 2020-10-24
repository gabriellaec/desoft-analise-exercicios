import random
a=1
total_de_dinheiro=10
while a>0 and total_de_dinheiro>0:
    print('saldo atual:{0}'.format(total_de_dinheiro))
    D1=random.randint(0,6)
    D2=random.randint(0,6)
    D3=random.randint(0,6)
    Ds=D1+D2+D3
    if total_de_dinheiro==0:
        a-=1
        print('Você perdeu!')
    else:
        h=0
        while h<1:
            d=input('Voce quer uma dica sim ou não, cada dica custa 1 ?')
            if d=='sim':
                total_de_dinheiro=total_de_dinheiro-1
                x=int(input('escolha um numero (1,18)'))
                y=int(input('escolha outro numero (1,18)'))
                z=int(input('escolha um ultimo numero (1,18)'))
                if x==Ds or y==Ds or z==Ds:
                    h+=1
                    print('Está entre os 3')
                else:
                    print('Não está entre os 3')
                print('saldo atual:{0}'.format(total_de_dinheiro))
            if d=='não':
                r=1
                while r>0 and total_de_dinheiro>0:
                    if total_de_dinheiro==0:
                        r-=1
                        print('Você perdeu!')
                    else:
                        g=int(input('chute um numero'))
                        if g==D4:
                            total_de_dinheiro=total_de_dinheiro*5
                        else:
                            total_de_dinheiro-=1
print('Você ganhou o jogo com {0} dinheiros!'.format(total_de_dinheiro))