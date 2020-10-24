a=int(input("Qual a distancia"))
if a <= 200:     
    x = a*0.5
    print('Preço da passagem é {0:.2f}'.format(x))

    
if a > 200:
    x = (200*0.5) + a*0.45
    print('Preço da passagem é {0:.2f}'.format(x))