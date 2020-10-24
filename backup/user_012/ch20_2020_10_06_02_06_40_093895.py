km= int(input('Qual a distancia: '))
if km <= 200:
    print(f' O valor cobrado é {km*0.50:.2f}')
else:
     print(f' O valor cobrado é {((km-200)*0.45)+200*0.50:.2f}')