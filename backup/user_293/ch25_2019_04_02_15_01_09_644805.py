distancia= float(input("Qual a distancia que voce deseja percorrer?: "))
if distancia <= 200:
    passagem= distancia*0.5
else:
    passagem= 100 + ((distancia - 200)*0.45)
print("O preço de sua passagem é R$ {0:.2f}".format(passagem))
                 
                 