import random
i = 100
while True:
    r = random.randint(0, 36)
    print (r)
    print ('Você possui {} fichas.'.format(i))
    aposta = int(input('Qual valor você quer apostar? '))
    if 0<aposta<=i:
        tipoaposta = input('A aposta é um numero ou uma paridade? n/p ') 
        if tipoaposta=='n':
            naposta = int(input('Digite o número apostado: '))
            if naposta==r:
                i= i + (aposta*35)
            else: 
                i= i-aposta
        elif tipoaposta=='p':
            paposta = input('Par ou impar: p/i ')
            if paposta=='p':
                if r%2==0:
                    i=i+aposta
                else:
                    i=i-aposta
            elif paposta=='i':
                if r%2!=0:
                    i=i+aposta*2
                else:
                    i=i-aposta
        else: 
            pass
    else:
        print('FIM')
        break
 