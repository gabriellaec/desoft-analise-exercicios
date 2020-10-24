distancia=float(input('Qual é a distância?')
preço1=distancia*0.50
preço2=(distancia-200)*0.45
if distancia<=200:
    print(preço1)
else:
    print(preço1+preço2)