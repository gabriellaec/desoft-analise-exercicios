from random import randint

dinheiro = 100
pergunta1 = input('Sua aposta é par ou paridade?')
pergunta2 = int(input('Digite um número de 1 a 36'))
pergunta3 = int(input('Quanto quer apostar?'))
while dinheiro > 0:
    print(pergunta1)
    if pergunta1 == 'n':
        print (pergunta3)
        print (pergunta2)
        sorteio = randint(1,36)
        if sorteio == pergunta2:
            dinheiro += 35*pergunta3
        else:
            dinheiro -= pergunta3
    elif pergunta1 == 'p':
        print (pergunta3)
        if pergunta3%2 == 0:
            dinheiro += 2*pergunta3
        else:
            dinheiro -= pergunta3
    elif pergunta1 == 'i':
        print(pergunta3)
        if pergunta3%2 != 0:
            dinheiro += 2*pergunta3
        else:
            dinheiro -= pergunta3
    else:
        print('Digite algo válido)
          
        
        