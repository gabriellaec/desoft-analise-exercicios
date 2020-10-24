passagem=0
distancia=int(input('qual a distancia a ser percorrida? '))
if distancia<=200:
    passagem=distancia*0.50
    print(format(passagem,'2f'))
else:
    passagem2=(distancia-200)*0.45 + 100
    print(format(passagem2,'2f'))
