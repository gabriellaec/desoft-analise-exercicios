d = int(input('Qual a distância que deseja percorrer?'))
if d <= 200:
    resultado = d*0.5
else:
    resultado = (d-200)*0.45 + 100
 print('O total da passagem é igual a {0:.2}'.format(resultado))
