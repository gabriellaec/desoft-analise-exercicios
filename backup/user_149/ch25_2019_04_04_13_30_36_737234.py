distancia=float(input('Qual distância irá percorrer? '))
if distancia<=200:
    valor1=distancia*0.5
    print(f'{valor1:.2f}')
if distancia>200:
    valor2=(distancia-200)*0.45
    print(f'{valor2+100:.2f}')
