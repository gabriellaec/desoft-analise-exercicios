inicial = float(input())
taxa = float(input())/100

saldo = inicial

for i in range(1, 25):
    
    saldo *= taxa
    
    decimos = int(saldo * 10 - int(saldo))
    centesimos = int(saldo * 100 - decimos * 10 - int(saldo) * 100)
    
    print('%d,%d%d' % (int(valor), decimos, centesimos))

aumento = saldo - inicial

decimos = int(aumento * 10 - int(aumento))
centesimos = int(aumento * 100 - decimos * 10 - int(aumento))
          
print('%d,%d%d' % (int(aumento), decimos, centesimos))