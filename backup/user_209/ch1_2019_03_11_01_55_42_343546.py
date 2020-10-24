def calcula_valor_devido (valor_emprestado,meses,juros):
    valor_emprestado = float(input("Digite o valor emprestado: "))
    meses = int(input("Digite a quantidade de meses: "))
    juros = juros/100
    calucla_valor_devido = valor_emprestado * (1+juros)**meses
    print ("Após ",m," meses, você deve R$" ,calcula_valor_devido)

    
