vel = int(input("Qual a vel? "))
if vel > 80:
    multa = (vel - 80)*5
    print("{0:.2f}").format(multa)
else:
    print("Não foi multado")