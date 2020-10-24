def calcula_valor_devido (valor_emprestado, n, tx_juros):
    valor_devido = valor_emprestado*(1+tx_juros)**n
    return (valor_devido)