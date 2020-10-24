velocidade = int(input())

excedente = velodiade - 80

if excedente > 0:
    multa = excedente * 5
    decimos = int(multa * 10 - int(multa) * 10)
    centesimos = int(multa * 100 - centesimos * 10 - int(multa) * 100)
    
    print('%d,%d%d' % (int(multa), decimos, centesimos)
else: print('Não foi multado')