import random
dinheiro=100
valor = 1
while dinheiro != 0 and valor != 0:
    print('Você possui {0} reais'.format(dinheiro))
    valor = int(input('Digite um valor:'))
    if valor != 0:
        aposta = input('A aposta é em um número(n) ou em paridade(p)?:')
        sorteio = random.randint(0,36)
        if aposta == 'n':
            numero = int(input('Digite um número de 1 a 36'))
            if numero == sorteio:
                dinheiro = dinheiro + valor*35
                print(dinheiro)
            else:
                dinheiro = dinheiro - valor
                print(dinheiro)
        elif aposta == 'p':
            par_impar = input('Digite p para par ou i para impar:')
            if sorteio %2 ==0:
                if par_impar == 'p':
                    dinheiro =  dinheiro + valor 
                    print(dinheiro)
                elif par_impar == 'i':
                    dinheiro = dinheiro - valor
                    print(dinheiro)
            elif sorteio %2 != 0:
                if par_impar=='i':
                    dinheiro = dinheiro + valor
                    print(dinheiro)
                else:
                    dinheiro = dinheiro - valor
                    print(dinheiro)
print('Game Over')