a = int(input('Qual a distância da viagem?'))
if a <= 200:
        y = a*0.5
else:
        y = 100+(a-200)*0.45
print ('{0:.2f}'.format(a))