def calcula_valor_devido(valor_emprestado,taxa_de_juros,número_de_meses):
    y=valor_emprestado+(valor_emprestado*taxa_de_juros)**número_de_meses
    return y
valor_emprestado=100
taxa_de_juros=0.05
número_de_meses=12
