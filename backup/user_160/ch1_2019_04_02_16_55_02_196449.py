def calcula_valor_devido

valor_emprestado = input("Qual o valor emprestado?")
num_mes = input("Qual o numero de meses?")
tx_juros = input("Qual a taxa de juros?")

i = 1
while i > num_mes:
   valor_emprestado = valor_emprestado * tx_juros 
i += 1

calcula_valor_devido = valor_emprestado