import random
valor = 100

while valor > 0:
    print(valor)
    aposta = int(input('Quanto você gostaria de apostar? '))
    solu = input('a aposta é em um número ou paridade (par/ímpar)?' )
    
    if aposta == 0:
        break
    dado = random.randint(0,36)
    if solu == 'n':
        num = int(input('Digite o número'))
        if num == dado:
            valor += aposta*35
        else: 
            valor -= aposta
    
    if solu == 'p':
        
        p_1 = input('O número é par ou ímpar?' )
        if dado%2 == 0:
            resposta = 'p'
        else: 
            resposta = 'i'
        if p_1 == resposta:
            valor += aposta
        else:
            valor -= aposta