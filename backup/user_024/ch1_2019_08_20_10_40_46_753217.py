def calcula_valor_devido(du,tx):
    pu = 1000/((1+(tx/100))**(du/252))
    return pu

