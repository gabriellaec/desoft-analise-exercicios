resposta= float(input('qual distancia deseja percorrer em km?'))
if resposta<=200km:
    preço= resposta*0.50
    print(preço)
    
else:
    preço= resposta*0.45
    print(preço)
