def calcula_valor_devido(valor_emprestado,número_de_meses,taxa_de_juros)
    calcula_valor_devido=valor_emprestado*(1+taxa_de_juros)**número_de_meses
    return calcula_valor_devido
print(calcula_valor_devido(1,3,5))

    
    
  