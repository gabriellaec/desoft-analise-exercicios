import random 
jogando = True 
sorteado = random.randint(0,36)
valor = 100
while jogando:
    print('Você tem {0} dinheiros!'.format (valor))
    if valor <= 0:
        print ('Você perdeu.')
        break
    valor_apostado = int(input('Qual valor você aposta?: '))
    if valor_apostado == 0:
        break
    pergunta_um = input('A aposta é em número ou paridade? [n/p]: ')
    if pergunta_um == 'n':
        pergunta_dois = int(input('Digite um número de 1 a 36: '))
        if sorteado == pergunta_dois:
            valor = valor + valor_apostado*35
        else:
            valor = valor - valor_apotado
    if pergunta_um == 'p':
        pergunta_tres = input('Escolha par ou ímpar[p/i]: ')
        if (pergunta_tres == 'p' and sorteado % 2 == 0) or (pergunta_tres == 'i' and sorteado %2 != 0):
            valor = valor + valor_apostado 
        else:
            valor = valor - valor_apostado
    sorteado = random. randint(0,36)