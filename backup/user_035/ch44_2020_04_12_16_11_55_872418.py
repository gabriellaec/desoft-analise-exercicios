x = input("Qual o nome do mês? ")
lista_mês = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
lista_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 0
while i <= len(lista_mês)-1:
    if lista_mês[i] == x:
        print(lista_n[i])
    else:
        i += 1