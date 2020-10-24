l_mes = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes = int(input("Mês? "))
for m in range(len(l_mes)):
    if mes == l_mes[m]:
        print(m)