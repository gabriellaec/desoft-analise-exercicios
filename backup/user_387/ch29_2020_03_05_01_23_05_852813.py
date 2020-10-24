deposito = float(input('deposito :'))
taxa = float(input('taxa :'))

saldo = deposito

t = 0
while t < 24:
    print(round(saldo,2))

    saldo = saldo * taxa

    t+=1
    
print(round(saldo - deposito,2))

    
    
