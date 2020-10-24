deposito = float(input('deposito :'))
taxa = float(input('taxa :'))

saldo = deposito

t = 0
while t < 24:
    print(round(saldo,2))

    saldo = saldo * (1+(taxa/100))

    t+=1
    
print(round(saldo - deposito,2))

    
    
