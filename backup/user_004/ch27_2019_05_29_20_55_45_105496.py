cigarros=int(input('Quantos cigarros por dia? '))
anos=int(input('Há quantos anos você fuma? '))

horasPerdidasDia=cigarros*10/60
tempoVidaPerdidoDias=horasPerdidasDias*(365*anos)

print('Você perdeu {:.0f} dias de vida'.format(tempoVidaPerdidoDias)
      
