inicial = float(input())
taxa = float(input())/100

saldo = inicial

for mes in range(1, 25):
    
    saldo *= taxa
    
    print('Saldo do mês %d é de R$%5.2f' % (mes, saldo))

aumento = saldo - inicial
          
print ("O ganho obtido com os juros foi de R$%8.2f." % (aumento))