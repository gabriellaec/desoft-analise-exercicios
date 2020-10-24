meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
i=0
while i < 12:
    mes = input('Qual o nome do mês? ')
    if mes == meses[i]:
        print(i+1)
    else:
        i+=1
