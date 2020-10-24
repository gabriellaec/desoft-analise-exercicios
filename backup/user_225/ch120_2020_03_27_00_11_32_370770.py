import random
dinheiro=100
while dinheiro>0:
    print('Seu crédito disponível é de R${0}'.format(dinheiro))
    aposta_inicial=int(input('Valor da aposta:'))
    if aposta_inicial <=0:
        dinheiro=0
    else:
        sort=random.randint(0,36)
        n_ou_paridade=input("Digite se é um número ou paridade: ")
        if n_ou_paridade == 'n':
            escolha_um_numero = int(input("Número de 1 a 36: "))
            if escolha_um_numero == sort:
                dinheiro+=35*aposta_inicial
                print('Seu crédito disponível é de R${0}'.format(dinheiro))
            else:
                dinheiro - aposta_inicial
                print('Seu crédito disponível é de R${0}'.format(dinheiro))
        if n_ou_paridade == 'p':
            par_ou_impar = input("É par ou ímpar: ")
            if par_ou_impar == "p":
                if sort%2 == 0:
                    dinheiro + aposta_inicial
                    print('Seu crédito disponível é de R${0}'.format(dinheiro))
                else:
                    dinheiro - aposta_inicial
                    print('Seu crédito disponível é de R${0}'.format(dinheiro))
        elif n_ou_paridade == 'i':
            if sort%2!=0:
                dinheiro + aposta_inicial
                print('Seu crédito disponível é de R${0}'.format(dinheiro))
            else:
                dinheiro - aposta_inicial
                print('Seu crédito disponível é de R${0}'.format(dinheiro))
print(sort)
    
                     
                     