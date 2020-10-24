valor= int(input("Valor a ser emprestado: "))
meses= int(input("Quantidade de meses: "))
taxa= float(input("Taxa: "))
def calcula_valor_devido(valor, meses, taxa):
    parcela= valor/meses
    valor_final= parcela*taxa
    return valor_final