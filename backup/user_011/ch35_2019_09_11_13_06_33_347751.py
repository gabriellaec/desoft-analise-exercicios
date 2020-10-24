deposito_i = float(input("Depósito inicial? "))
deposito_m = float(input("Depósito mensal? "))
tx_juros = float(input("Taxa de juros poupança? "))

i = 0
montante_i = (deposito_i)*(1+tx_juros)
montante = (deposito_m + montante_i)*(1+tx_juros)

while i < 23:
    montante = montante + (montante - deposito_i)*(1+tx_juros)
    print(montante)
    i+=1
    