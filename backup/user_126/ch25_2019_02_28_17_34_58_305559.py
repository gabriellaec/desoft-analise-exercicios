km = int (input('km:'))
if km <200:
    valor =km*0.5
else:
    valor = (km-200)*0.45+200*0.5
print(valor)