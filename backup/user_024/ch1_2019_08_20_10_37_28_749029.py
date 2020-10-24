def calcula_valor_devido(du,tx):
    pu = 1000/((1+(tx/100))**(du/252))
    return pu

tx = float(input("qual a taxa?"))
du = int(input("quantos dias uteis?"))

y = calcula_valor_devido
print("o titulo vale {0}" .format(y(du,tx)))