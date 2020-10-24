deposito_inicial = float(input('Digite o depósito inicial: '))
taxa = float(input('Digite a taxa de juros: '))

for t in range(1,25):
    print ("%.2f" %(deposito_inicial*(1 + taxa)**t))
    
print ('%.2f' %(deposito_inicial*(1 + taxa)**24 - deposito_inicial))