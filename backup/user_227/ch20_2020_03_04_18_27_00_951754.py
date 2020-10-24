distancia = float(input("Qual a distância que você quer percorrer? "))
if distancia <= 200:
    print("Multa é R${0:.2f}".format(distancia*0.5))
else:
    print("Multa é R${0:.2f}".format((distancia - 200)*0.45 + 100)) 