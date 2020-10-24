def calcula_valor_devido (valor_emprestado , n_meses , taxa_juros):
    
    juros_compostos = valor_emprestado*(1+(taxa_juros/100))**n_meses
    
    return juros_compostos

x = 1500
y = 10
z = 1


print(calcula_valor_devido(x,y,z))