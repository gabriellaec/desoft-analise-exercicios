distancia = float(input ("Qual? "))
if distancia <= 200:
    a = distancia*0.5
    print(f'{a:.2f}')
else:
   	print('{:.2f}'.format(100+(distancia-200)*0.45))