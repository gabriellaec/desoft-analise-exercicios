import random

saldo =100

while saldo > 0:
    print (saldo)
    aposta = float(input('Quanto você aposta ?: '))
    resposta = input('A aposta é um número ou paridade ?: ')
    if aposta==0:
        break
    dado = random.randint(0,36)
    if resposta =='n':
        num=int(input('Digite o múmero: '))
        if num == dado :
           saldo+=aposta*35
        else:
            saldo -= aposta 
    if resposta =='p':
        P= input('O número é par ou ímpar ?: ')
        if dado % 2 == 0:
            resp='p'
        else:
            resp='i'
        if P == resp:
            saldo += aposta
        else:
            saldo -= aposta


