m = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
mes = input("nome do mês?")

i = o
while i < len(m):
    if m[i] == mes:
        i=+1
        print(i+1)
    