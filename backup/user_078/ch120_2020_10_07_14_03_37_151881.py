dinheiro = 100

while dinheiro > 0:

    print('Você possui {0} de dinheiro disponível!'.format(dinheiro))

    aposta_valor = int(input('Quanto você quer apostar? (0 para sair)' ))

    if aposta == 0:
        break

    else:

        sorteio = random.randint(1, 36)

        aposta_ParImpar = str(input('Você aposta número ou paridade? (n/(p/i)): '))

        if aposta_ParImpar == 'n':

            algum_numero = str(input('Qual número irá cair? '))

            # numeros = range(1, 37)
            # sorteio = numeros.sort()

            if algum_numero == sorteio:
                dinheiro += aposta_valor * 35

            else:
                dinheiro -= aposta_valor

        elif aposta_ParImpar == 'p':
            if sorteio%2 == 0:
                dinheiro += aposta_valor
            else:
                dinheiro -= aposta_valor
        
        elif aposta_ParImpar == 'i':
            if sorteio%2 != 0:
                dinheiro += aposta_valor
            else:
                dinheiro -= aposta_valor