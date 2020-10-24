def calcula_valor_devido(valor,meses,taxa):
        montante=valor*(1+taxa)**meses
        return montante
print(calcula_valor_devido(1000,3,0.1))