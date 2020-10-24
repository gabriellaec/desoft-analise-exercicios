def calcula_valor_devido(x, z, w):
    y = x*((1+z)**w)
    return y
valor_emprestado = 1000
número_de_meses = 2
taxa_de_juros = 0.1
print (calcula_valor_devido(valor_emprestado, número_de_meses, taxa_de_juros))
