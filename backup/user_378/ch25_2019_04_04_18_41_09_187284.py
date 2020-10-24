d=int(input('Qual é a distância?'))
preço_1=d*0.5
preço_2=(d-200)*0.45
if d<=200:
    print(float(d*0.5))
else:
    print(float(100+preço_2))