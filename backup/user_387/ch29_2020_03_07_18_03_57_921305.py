deposito = float(input('deposito :'))
taxa = float(input('taxa :'))

saldo = deposito

for ele in range(0,24):

    saldo = saldo * (1 + taxa)
    print("{0:.2f}".format(saldo))
    

print("{0:.2f}".format(saldo - deposito))


    
    
