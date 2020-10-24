nome_mes = input('Qual o nome do mes?')
nome_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
i=0
while i < 12:
    if nome_meses[i] == nome_mes :
        print (i+1)
    i += 1