mes = ['0', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
pergunta = input("digite um mês por extenso: ")

i = 0 
while i <= 12:
    if pergunta == mes[i]:
        print(i)
    i += 1
