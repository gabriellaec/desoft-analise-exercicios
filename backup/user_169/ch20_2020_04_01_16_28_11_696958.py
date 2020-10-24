distancia=float(input("Qual a distancia que quer percorrer?"))

if distancia<=200:
    print(distancia*0.5, 'reais')
    
elif distancia>200:
    print((distancia-200)*0.45+(200*0.5), 'reais')