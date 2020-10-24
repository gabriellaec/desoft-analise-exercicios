distancia = int(input("Qual distancia deseja percorrer? "))
def valor(distancia):
    if distancia<200:
        valor1=distancia * 0.5
    print ("O valor sera de {0:.2f}".format(valor1))
    else:
        valor2=(distancia-200)* 0.45 + 100
    print ("O valor sera de {0:.2f}".format(valor2))
        
                                