import math

def calcula_valor_devido(valor_emprestado, numero_De_meses, taxa_De_juros):
    Juros=valor_emprestado*(1 + taxa_De_juros)**numero_De_meses
    
    return Juros
