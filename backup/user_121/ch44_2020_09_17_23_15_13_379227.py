meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mes=input('Qual o nome do mês? ')
i=0
while i<12:
    if meses[i]==mes:
        break
    i+=1
print(i+1)