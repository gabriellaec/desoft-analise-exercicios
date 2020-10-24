def calcula_valor_devido(valor_emprestado,número_de_meses, taxa_de_juros): 
    if número_de_meses==0:
        return valor_emprestado
    else:
        valor_dev=valor_emprestado*(1+taxa_de_juros)^número_de_meses
        return valor_dev
    