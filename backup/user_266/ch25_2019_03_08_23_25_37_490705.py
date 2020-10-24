d = float(input('Qual a distância que você deseja percorrer? '))
if d <= 200:
    p1 = d*0.5
    print('O valor da passagem é R${0:.2f}'.format(p1))
else:
    p2 = 0.45*(d-200) + 100
    print('O valor da passagem é R${0:.2f}'.format(p2))