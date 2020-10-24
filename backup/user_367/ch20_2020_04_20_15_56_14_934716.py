Q= float(input('Qual a distancia? '))
if Q <= 200:
    i= Q * 0.50
else:
    i= Q * 0.95
print('O preço é {0:.2f}' .format(i))
