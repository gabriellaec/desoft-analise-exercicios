
def calcula_valor_devido(valor_emprestado, numero_de_meses, taxa_de_juros):
    a=valor_emprestado
    b=numero_de_meses
    c=taxa_de_juros
    s=a*(1+c)**b
    return s                 

print('valor final é {0}'.format(calcula_valor_devido(2000,10,10)))