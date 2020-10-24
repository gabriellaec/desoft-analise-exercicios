mes = ['Começo', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro', 'Fim']
numero = ['inicio',1,2,3,4,5,6,7,8,9,10,11,12]
nome = input("Qual o nome do mês?")
pergunta = True
i = 0
while pergunta:
    if nome == mes[i]:
        print(numero[i])
        x =False
    else:
        i+=1
    