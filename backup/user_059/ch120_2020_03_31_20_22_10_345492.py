import random
r = random.randint(1;36)
i = 100
print ('Você possui {} fichas.'.format(i))
while True:
    aposta = int(input('Qual valor você quer apostar? '))
    if aposta<i:
        if aposta>0:
            tipoaposta = input('A aposta é um numero ou uma paridade? n/p) ') 
            if tipoaposta=='n':
                naposta = input('Digite o número apostado: ')
                if naposta==r:
                    i = i + (aposta*35)
                else: 
                    i = i-aposta
            elif tipoaposta=='p':
                paposta = input('Par ou impar:(p/i) ')
                if paposta=='p':
                    if r%2==0:
                        i = i+aposta*2
                    else:
                        i = i-aposta
                if paposta=='i':
                    if r%2!=0:
                        i = i+aposta*2
                    else:
                        i = i-aposta
        else:
            break
    else:
        break