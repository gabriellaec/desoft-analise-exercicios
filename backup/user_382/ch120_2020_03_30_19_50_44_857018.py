import random 

saldo = 100


while saldo != 0:
    print ('Você tem {} de dinheiro'.format(saldo))
    aposta = int(input('Quanto você aposta?'))
    resp = input('A aposta é um número ou paridade?')
    
    if aposta == 0:
        break
    
    if resp == 'n':
        num = int(input('Digite o número'))
        if num == random.randint(0,36):
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
        
        