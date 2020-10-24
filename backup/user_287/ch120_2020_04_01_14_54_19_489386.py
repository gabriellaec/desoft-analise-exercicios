from random import randint
saldo = 100
aposta = int(input('aposte em um valor'))
x = str(input('Numero ou paridade?:'))
if aposta==0:
    print('fim')
elif x=='n':
    j = randint(0,36)
    if aposta == j:
        saldo = saldo + 35*aposta
    elif aposta != j:
        saldo = saldo - aposta
elif x=='p':
    j = randint(0,36)
    t = str(input('Par ou Impar'))
    if j%2==0 and t=='p' or j%2!=0 and t!='p' :
        saldo = saldo+aposta
    else:
        saldo = saldo-aposta
    print(saldo)
        
        
    


