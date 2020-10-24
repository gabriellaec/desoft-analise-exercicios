distancia=float(input('Qual distância deseja percorrer? '))
if distancia<=200:
    print ('O preço da passagem é {0}R$'.format(distancia*0,50))
else:
    print ('O preço da passagem é {0}R$'.format((distancia*0,50)+(distancia-200)*0,45))
        