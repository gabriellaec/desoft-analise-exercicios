km = float(input('Qual a distância a ser percorrida em km? '))
if km <= 200:
    print('{0:.2f}'.format(km*0.5))
elif km > 200:
    print('{0:.2f}'.format((km*0.5)+(km-200)*0.45))