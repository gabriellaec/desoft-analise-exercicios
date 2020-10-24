deposito_i = float(input("Valor do deposito? "))
tx_juros = float(input("Valor dos juros? "))

i = 1
montante = deposito_i
while i <= 24:
    montante = montante + montante*tx_juros
    i += 1
    print("{0:.2f}".format(montante))
    
lucro = montante - deposito_i
print("{0:.2f}".format(lucro))
    
                   