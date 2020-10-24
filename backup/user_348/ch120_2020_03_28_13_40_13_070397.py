from random import randint
dinheiro = 100
print(dinheiro)
jogo = True
a = randint(1,36)
while jogo:
    valor = float(input('aposte um valor:'))
    while valor > 0:
        aposta = input('numero ou paridade:')
        if aposta == 'n':
            numero =  int(input('Escolha um numero:'))
            if numero == a:
                dinheiro = dinheiro + 35*valor
            else:
                dinheiro = dinheiro - 10
        elif aposta == 'p':
             escolha = input('p ou i:')
            if a%2 == 0 and escolha == 'p':
                 dinheiro = dinheiro + valor
            elif a%2 != 0 and escolha == 'i':
                dinheiro = dinheiro + valor
            else:
                dinheiro = dinheiro - valor
print(dinheiro)