meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
nome = input('Qual o nome do mes: ')
for a in meses:
    if nome == meses[meses.index(a)]:
        print (meses.index(a) + 1)