mes = (input('Qual o nome do mês?'))
meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
i = 0
while True:
    if mes == meses[i]:
        print(i + 1)
        False
    else:
        i += 1