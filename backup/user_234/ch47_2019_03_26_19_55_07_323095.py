meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

n_mes = int(input("Qual o número do mês?: "))


if n_mes >= 0:
    print(meses[n_mes-1])