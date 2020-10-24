velo = int(input("Qual sua velocidade?"))
if velo > 80:
    multa = (velo-80)*5
    print ("Você foi multado:{multa:4.2}")
else:
    print ("Não foi multado")