depósito_inicial= input(" depósito inicial :")
taxa_de_juros= input(" taxa de juros :")
contador=0
ganho=0
valor_total=0
while contador<24:
    ganho += depósito_inicial * taxa_de_juros *contador
  	valor_total = depósito_inicial + ganho
    print(valor_total)
    contador+=1