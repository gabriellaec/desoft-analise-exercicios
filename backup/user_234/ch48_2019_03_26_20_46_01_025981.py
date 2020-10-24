meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

nome_mes = input("Qual o nome do mes?: ")

i=0
n_mes = 1

while nome_mes != meses[i]:
    i+=1
    n_mes+=1
print(n_mes)