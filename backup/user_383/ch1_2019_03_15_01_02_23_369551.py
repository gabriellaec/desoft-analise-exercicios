def calcula_valor_devido(valor_emprestadp,número_de_meses,taxa_de_juros):
    juros=valor_emprestado*(1+taxa_de_juros)**(número_de_meses)
    return juros