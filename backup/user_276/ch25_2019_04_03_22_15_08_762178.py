a = float(input('Distância a ser percorrida:   '))
if a <= 200:
    print('{:0.2f}'.format(a*0.50))
else:
    print('{:0.2f}'.format(100 + (a-200)*0.45))