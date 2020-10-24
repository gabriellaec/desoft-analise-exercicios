mes = ['Começo', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro', 'Fim']
pergunta = True
while pergunta:
    numero = int(input("Qual o mês?: "))
    if numero + 1 == mes[i]:
        print(mes[i])
        pergunta = False
    else:
        print("Esse número não é compatível a nenhum mês.")