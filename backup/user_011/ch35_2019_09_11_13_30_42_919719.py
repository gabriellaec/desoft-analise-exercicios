deposito_i = float(input("Depósito inicial? "))
deposito_m = float(input("Depósito mensal? "))
tx_juros = float(input("Taxa de juros poupança? "))

i = 0
poupança = deposito_i


while i < 24:
    poupança = (poupança)*(1+tx_juros) + deposito_m 
    print(poupança)
    i+=1
    
print(poupança - (deposito_i + 24*deposito_m))
    