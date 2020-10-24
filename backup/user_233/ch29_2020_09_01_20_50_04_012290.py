inicial = float(input())
taxa = float(input())/100 + 1

saldo = inicial

print('%.2f' % saldo)

for mes in range(2, 25):
    
    saldo *= taxa
    
    print('%.2f' % saldo)

aumento = saldo - inicial
          
print ('%.2f' % (aumento))