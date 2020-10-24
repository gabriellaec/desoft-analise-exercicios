    mes=input("Qual o nome do mês?: ")
    meses= ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    for e in range(len(meses)):
        if meses[e]==mes:
            print e+1