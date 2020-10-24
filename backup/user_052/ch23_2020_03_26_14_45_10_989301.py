velo = int(input("Qual sua velocidade?"))
if velo > 80:
    multa = (velo-80)*5
    print ("Você foi multado:{multa:.2f}")
else:
    print ("Não foi multado")