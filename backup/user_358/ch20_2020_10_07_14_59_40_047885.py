distancia=int(input('qual distancia voce deseja percoirrer? '))

if distancia<=200:
    valor=distancia*0.50
    print (f'{valor:.2f}')
    
else:
    valor_extra=((distancia-200)*0.45)+100
    print(f'{valor_extra:.2f}')