deposito = int(input("Dinheiro depositado?: "))
taxa = float(input("Qual a taxa da poupança?: "))


i = 1
while i < 25:
    montante = deposito*(1 + (taxa/100))**i
    i+=1
    print ("{:.2f}".format(montante))

print("Valor acumulado foi de: {:.2f}".format(montante - deposito), "reais")