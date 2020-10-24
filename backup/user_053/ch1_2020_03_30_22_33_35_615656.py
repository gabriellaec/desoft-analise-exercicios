def calcula_valor_devido(valor_emprestado, meses, taxa_juros):
    valor_total = (valor_emprestado)*((1 + taxa_juros)**meses)
    return valor_total

emprestimo = 50000
tempo = 24
juros = 0.05

print(calcula_valor_devido(emprestimo, tempo, juros))