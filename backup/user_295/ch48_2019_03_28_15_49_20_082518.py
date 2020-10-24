nome_do_mes = int (input("Qual é o nome do mes? "))

lista = [0, "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
t = 0
while t < len(lista):
    if nome_do_mes == lista[t]:
        print(t)
    