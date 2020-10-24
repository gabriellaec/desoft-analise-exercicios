distancia = int(input("Quantos quilometros você vai percorrer? "))
passagem = distancia*0.5
passagem1 = distancia*0.5 + (distancia-200)*0.45
if distancia < 200:
    print("O valor da passagem será de R$ {0:.2f}".format(passagem))
else:
    print("O valor da passagem será de R$ {0:.2f}".format(passagem1))
    
    
    

                