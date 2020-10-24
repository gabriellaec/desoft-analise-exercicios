inicial = float(input())
taxa = float(input()/100)

aumento = 0
anterior = inicial

for i in range(1, 25):
    
    valor = inicial * taxa ** i
    aumento += valor - anterior
    
    decimos = int(valor * 10 - int(valor))
    centesimos = int(valor * 100 - decimos * 10 - int(valor) * 100)
    
    print('%d,%d%d' % (int(valor), decimos, centesimos))

decimos = int(aumento * 10 - int(aumento))
centesimos = int(aumento * 100 - decimos * 10 - int(aumento))
          
print('%d,%d%d' % (int(aumento), decimos, centesimos))