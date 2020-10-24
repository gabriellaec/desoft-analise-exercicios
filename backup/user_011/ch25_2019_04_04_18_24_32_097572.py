distancia=int(input('Qual a distancia percorrida? '))
if distancia<=200:
    preço=0.5*distancia
    print(float(preço))
else:
    if distancia>200:
        preço=(distancia - 200)*0.45 + 200*0.5
        print(float(preço))
        
  