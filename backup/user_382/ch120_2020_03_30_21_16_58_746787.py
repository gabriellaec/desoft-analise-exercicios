import random 

saldo = 100


while saldo > 0:
    print (saldo)
    aposta = float(input('Quanto você aposta?'))
    resp = input('A aposta é um número ou paridade?')
    
    if aposta == 0:
        break
    dado = random.randint(0,36)
    if resp == 'n':
        num = int(input('Digite o número'))
        if num == dado:
            saldo += aposta*35
        else:
            saldo -= aposta
    
    if resp == 'p':

        p_i = input('O número é par ou impar?')
        if dado % 2 == 0:
            resposta = 'p' 
        else:
            resposta = 'i'
        if p_i == resposta:
            saldo += aposta
        else:
            saldo -= aposta
        