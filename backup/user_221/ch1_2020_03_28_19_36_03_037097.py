def calcula_valor_devido(valor_emprestado, numero_de_meses, taxas_de_juros):
    return valor_emprestado * ((1+taxas_de_juros)**(numero_de_meses))
                       