p=float(input('Qual a distancia? '))
if p<=200:
    print('A passagem custa R$ {:.2f}'.format(p*0.5))
if p>200:
    print('A passagem custa R$ {:.2f}'.format(100+(p-200)*0.45))