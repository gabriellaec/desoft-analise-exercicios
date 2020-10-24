mes = ['Começo', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro', 'Fim']
nome = input("Qual o nome do mês?")
for i in range (len(mes)):
    if nome == mes[i]:
        print(i)
        
    