def calcula_valor_devido(emprestimo,meses,taxa):
    if emprestimo==0 or meses==0 or taxa==0:
        valor_devido=0
    else: 
        valor_devido=emprestimo*(taxa*meses)
    return valor_devido