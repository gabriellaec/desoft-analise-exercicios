lista_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista_nome = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes = str(input("Me fale o nome do mes, te falo o numero: "))
x = 0
while x < 12:
    if mes == lista_nome[x]:
        print("Esse é o mês ",lista_mes[x])
    x += 1