#Exemplo de um empréstimo de R$1000,00, com taxa de 2% a.m., com dívida por 10 meses

def calcula_valor_devido(valor_emprestado, número_de_meses, taxa_de_juros):
    y = valor_emprestado * (1 + taxa_de_juros)**número_de_meses
    return y
a = 1000
b = 10
c = 0.02
d = calcula_valor_devido(a, b, c)
print(d);