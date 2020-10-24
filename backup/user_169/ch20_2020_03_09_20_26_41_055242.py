distancia=float(input("Qual a distancia que quer percorrer?"))

if distancia<=200:
    print(distancia*0.5)
    
elif distancia>200:
    print((distancia-200)*0.45)