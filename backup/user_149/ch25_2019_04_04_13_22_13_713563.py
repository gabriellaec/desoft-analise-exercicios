distancia=int(input('Qual distância irá percorrer? '))
if distancia<=200:
    valor1=distancia*0.5
    print(valor1)
if distancia>200:
    valor2=(distancia-200)*0.45
    print(100+valor2)