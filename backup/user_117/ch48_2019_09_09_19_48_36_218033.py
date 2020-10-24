m = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
mes = input("nome do mês?")

for i in range(len(m)):
    if m[i] == mes:
        print(i+1)