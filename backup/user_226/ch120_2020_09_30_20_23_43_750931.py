import random
dinheiro = 100

while dinheiro > 0:
    print(f'Sua carteira é de {dinheiro}')
    aposta = int(input('Qual o valor da sua aposta? '))
    if aposta == 0:
        break
    opcao = input('A opção da aposta é qual? (n/p) ')
    if opcao == 'n':
        apostan = int(input('Qual a sua aposta? '))
        valor = random.randint(0, 36)
        if valor == apostan:
            dinheiro += aposta * 35
        else:
            dinheiro -= aposta
    elif opcao == 'p':
        apostap = input('par ou impar? ')
        valor = random.randint(0, 36)
        if apostap == 'p' and valor % 2 == 0 or valor == 0:
            dinheiro += aposta
        elif apostap == 'i' and valor % 2 != 0:
            dinheiro += aposta
        else:
            dinheiro -= aposta
