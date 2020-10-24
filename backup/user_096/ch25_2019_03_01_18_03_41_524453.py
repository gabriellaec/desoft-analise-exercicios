passagem=0
distancia=int(input('qual a distancia a ser percorrida? '))
if distancia<=200:
    passagem=distancia*0.50
    print(round(passagem,2))
else:
    passagem2=(distancia-200)*0.45 + 100
    print(round(passagem2,2))
