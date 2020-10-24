meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

n_mes = int(input("Qual o número do mês?: ")


if n_mes >= 0:
    return meses[n_mes+1]