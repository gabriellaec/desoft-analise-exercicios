distancia = int(input('Qual a distancia percorrida em Km?:'))   
if distancia <200:
    total =(distancia * 0.5)
    print('O preço da passagem é R$ {0:.2f}'.format(total))
else:
    final = ((distancia * 0.5) + (distancia - 200) * 0.45)
    print('O preço da passagem é R$ {0:.2f}'.format(final))  
