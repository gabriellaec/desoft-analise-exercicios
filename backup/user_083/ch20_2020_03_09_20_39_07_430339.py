a=int(input('qual a distancia da sua viagem: '))
if a <=200:
    b = a*0.5
else:
    b = 0.5*200+(a-200)*0.45
print('{0:.2f}'.format(b))