mes = ['Começo', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro', 'Fim']
pergunta = True
while pergunta:
    numero = int(input("Qual o mês?: "))
    if numero + 1 == mes[i]:
        print(mes[i])
        pergunta = False
    else:
        print("Esse número não é compatível a nenhum mês.")