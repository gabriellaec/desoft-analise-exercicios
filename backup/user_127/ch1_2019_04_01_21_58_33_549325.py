def calcula_valor_devido(emprestado, meses, juros):
    valor = emprestado * (1 + juros) ** meses
    return(valor)