distancia = float(input ('Qual distancia deseja percorrer? '))
if distancia <= 200:
    print('Valor da passagem: R$ {0:.2f}'.format(distancia*0.50))
else:
    print('Valor da passagem: R$ {0:.2f}'.format((distancia-200)*0.45+100))