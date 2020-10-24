ano = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes = int(input("que mês é este? "))
if mes > 0 and mes < 13:
    print(ano[mes-1])