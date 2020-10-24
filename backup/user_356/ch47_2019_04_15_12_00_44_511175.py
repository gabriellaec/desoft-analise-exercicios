lista_mes=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
n=int(input("Digite o número do mês desejado: "))
for i in range(len(lista_mes)):
    if i+1==n:
        print(lista_mes[i])
        break