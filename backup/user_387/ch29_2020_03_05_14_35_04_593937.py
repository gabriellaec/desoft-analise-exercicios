deposito = float(input('deposito :'))
taxa = float(input('taxa :'))

saldo = deposito

t = 0
while t < 23:
    print(round(saldo,2))

    saldo = saldo * (1 + taxa)

    t+=1
    
print(round(saldo - deposito,2))

    
    
