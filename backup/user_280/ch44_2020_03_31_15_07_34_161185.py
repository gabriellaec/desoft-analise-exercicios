meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
i=0
mes = str(input('Qual o nome do mês? '))
while i < 12:
    if mes == meses[i]:
        print(i+1)
    else:
        i+=1