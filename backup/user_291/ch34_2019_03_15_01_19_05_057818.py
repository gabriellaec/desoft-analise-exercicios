depósito = int(input("Qual é o depósito? ")

taxa_de_juros = int(input("Qual é a taxa de juros? ")
                    
i = 1

dinheiro = 0

while i <= 24:
	dinheiro = depósito*(1+taxa_de_juros)**24
    print(dinheiro)
    
