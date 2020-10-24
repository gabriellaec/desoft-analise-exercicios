mes = (input('Qual o nome do mês?'))
meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
i = 0
while mes != meses[i] and i <= 12:
    i += 1
if mes == meses[i]:
    print(i + 1)