from random import randint
dinheiro = 100
a = randint(1,36)
while dinheiro > 0:
    print(a)
    valor = float(input('aposte um valor:'))
    if valor <= 0:
        dinheiro = 0
    else:
        aposta = input('numero ou paridade:')
        if aposta == 'n':
            numero =  int(input('Escolha um numero:'))
            if numero == a:
                dinheiro = dinheiro + 35*valor
                print(dinheiro)
            else:
                dinheiro = dinheiro - 10
                print(dinheiro)
        elif aposta == 'p':
             escolha = input('p ou i:')
            if escolha == 'p':
                if a%2 == 0:
                    dinheiro = dinheiro + valor
                    print(dinheiro)
                else:
                    dinheiro = dinheiro - valor
            elif escolha == 'i':
                if a%2 != 0:
                dinheiro = dinheiro + valor
                 print(dinheiro)
            