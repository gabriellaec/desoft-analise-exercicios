def calcula_valor_devido(valor_emprestado, número_de_meses, taxa_de_juros):
    montante=valor_emprestado*(1+taxa_de_juros)**número_de_meses
    return (montante)

print(calcula_valor_devido(100000,48,0.035))