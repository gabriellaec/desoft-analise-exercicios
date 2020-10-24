distancia = float(input("Quantos quilometros você vai percorrer? "))
if distancia < 200:
    passagem = distancia*0.5
    print("O valor da passagem será de R$ {0:.2f}".format(passagem))
else:
    passagem = distancia*0.5 + (distancia-200)*0.45
    print("O valor da passagem será de R$ {0:.2f}".format(passagem))
    
    
    

                