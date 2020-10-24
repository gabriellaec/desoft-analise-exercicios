import random as r 

saldo = 100
print('Você tem {0}'.format(saldo))

while saldo != 0:
    aposta = int(input('Quanto você aposta?'))
    resp = input('A aposta é um número ou paridade?')
    
    if resp == 'n':
        num = int(input('Digite o número'))
        if num == random.randint(1,36):
            saldo += aposta*num
        else:
            saldo -= aposta
    
    if resp == 'p':
        num = random.randint(0,36)
        p_i = input('O número é par ou impar?')
        if random.randint(0,36) % 2 == 0:
            resposta = 'p' 
        else:
            resposta = 'i'
        if p_i == resposta:
            saldo += aposta
        else:
            saldo -= aposta
        
        