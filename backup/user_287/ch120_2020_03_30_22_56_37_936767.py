saldo = 100
saldo_novo = saldo
while saldo > 0:
    print(saldo)
aposta = int(input('aposte em um valor'))
x = str(input('Numero ou paridade?:'))
if x==0:
    return False
elif x==n:
    j = random.randint(1,36)
    if aposta == j:
        saldo_novo = saldo + 35*aposta
    elif aposta != j:
        saldo_novo = saldo - aposta
elif x==p:
    j = random.randint(1,36)
    t = str(input('Par ou Impar'))
    if t == p:
        
        
        
    


