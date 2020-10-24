veloc = float(input("Qual a velocidade do carro: "))
if veloc>80:
    multa = (veloc-80)*5
    round(multa,2)
    print(multa)
else:
    print("Não foi multado")