valor_emprestado = int(input ('Quanto foi emprestado? '))
numero_de_meses = int(input ('Quantos meses durou o empréstimo? '))
taxa_de_juros = int(input ('Qual a taxa de juros estabelecida, em %? (na forma XX)'))

def calcula_valor_devido(valor_emprestado, taxa_de_juros, numero_de_meses):
    y = valor_emprestado*((1+(taxa_de_juros)/100)**(numero_de_meses))
    return y

print (calcula_valor_devido(valor_emprestado, taxa_de_juros, numero_de_meses))