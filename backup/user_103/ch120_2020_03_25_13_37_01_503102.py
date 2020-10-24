import random
sort=random.randint(0,36)
dinheiro=100
while dinheiro>0:
    print('Seu crédito disponível é de R${0}'.format(dinheiro))
    aposta_inicial=int(input('Valor da aposta:'))
    if aposta_inicial <=0:
        dinheiro=0
    else:
        n_ou_paridade=('Digite se a aposta é em número ou paridade:')
        if n_ou_paridade=='n':
            escolha_um_numero=int(input('Digite um numero de 1 a 36:'))
            if escolha_um_numero==sort:
                dinheiro+=35*aposta_inicial
                print ('Seu crédito é de R${0}'.format(dinheiro))
            else:
                dinheiro-=aposta_inicial
                print('Seu crédito é de R${0}'.format(dinheiro))
        if n_ou_paridade=='p':
            escolha_par_ou_impar=int(input('par ou impar?:'))
            if escolha_par_ou_impar=='p':
                if sort%2==0:
                    dinheiro+=aposta_inicial
                    print('Seu crédito é de R${0}'.format(dinheiro))
                else:
                    dinheiro-=aposta_inicial
                    print ('Seu crédito é de R${0}'.format(dinheiro))
            elif escolha_par_ou_impar=='i':
                if sort%2!=0:
                    dinheiro+=aposta_inicial
                    print('Seu crédito é de R${0}'.format(dinheiro))
                else:
                    dinheiro-=aposta_inicial
                    print('Seu crédito é de R${0}'.format(dinheiro))
