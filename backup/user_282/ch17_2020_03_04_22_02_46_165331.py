Ano = int(input('Ano: '))

if (Ano%4==0 and Ano%100!=0) or (Ano%400==0):
    print('True')
else:
    print('False')