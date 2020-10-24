distancia=int(input('Qual é a distância?')
preço_1=distancia*0.50
preço_2=(distancia-200)*0.45
if distancia<=200:
    print(float(preço_1))
else:
    print(float(100+preço_2))