def calcula_valor_devido(emprestimo,meses,taxa):
    i=0
    valor_devido=emprestimo
    while i<meses:
        valor_devido+=valor_devido*taxa
        i+=1
    return valor_devido