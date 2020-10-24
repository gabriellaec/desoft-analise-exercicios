soma = 0 
deposito = float(input("valor do deposito:"))
juros = float(input("taxa de juros:"))
rend = deposito*juros
for c in range (0,25):
    soma = soma + rend
    print (rend)
print (soma)