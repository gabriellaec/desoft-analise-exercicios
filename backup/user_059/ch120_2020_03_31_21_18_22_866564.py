import random
while True:
    r = random.randint(1, 37)
    i = 100
    print ('Você possui {} fichas.'.format(i))
    aposta = int(input('Qual valor você quer apostar? '))
    if aposta<i:
        if aposta>0:
            tipoaposta = input('A aposta é um numero ou uma paridade? n/p ') 
            if tipoaposta=='n':
                naposta = int(input('Digite o número apostado: '))
                if naposta==r:
                    i = i + (aposta*35)
                else: 
                    i = i-aposta
            elif tipoaposta=='p':
                paposta = input('Par ou impar: p/i ')
                if paposta=='p':
                    if r%2==0:
                        i = i+aposta*2
                    else:
                        i = i-aposta
                elif paposta=='i':
                    if r%2!=0:
                        i = i+aposta*2
                    else:
                        i = i-aposta
        else:
            print('FIM')
            break
    else:
        print('FIM')
        break
 