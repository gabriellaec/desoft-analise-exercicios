#0.5/km até 200km e 0.45 depois 
distancia=float(input('Qual a distância em km que você deseja percorrer? '))
valor1=distancia*0.5
valor2=distancia*0.45

if distancia<=200:
    print('O valor da passagem é: {0}'.format(valor1))
else:
    print('O valor da passagem é: {0}'.format(valor2))