nome_mes = input("Qual o nome do mês?: ")
lista_nome_mes = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
i = 1
while nome_mes != lista_nome_mes[i - 1]:
    i += 1
print (i)