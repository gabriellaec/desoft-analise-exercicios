x=input("Qual a distância você deseja percorrer em km? ")
if x<=200:
        print("O valor da passagem é {0:.2f}".format(float(x*0.5)))
else:
        print("O valor da passagem é {0:.2f}".format(float(x*0.45)))
    