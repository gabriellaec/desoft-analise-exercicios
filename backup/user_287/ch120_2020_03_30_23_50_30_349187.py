import math
saldo = 100
saldo_novo = saldo
aposta = int(input('aposte em um valor'))
x = str(input('Numero ou paridade?:'))
if x==0:
    print('fim')
elif x=='n':
    j = random.randint(1,36)
    if aposta == j:
        saldo_novo = saldo + 35*aposta
    elif aposta != j:
        saldo_novo = saldo - aposta
elif x=='p':
    j = random.randint(1,36)
    t = str(input('Par ou Impar'))
    if j%2==0 and t=='p' or j%2!=0 and t!='p' :
        saldo_novo = saldo+aposta
    else:
        saldo_novo =saldo-aposta
print(saldo)
        
        
        
    


