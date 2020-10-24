n = int(input('Digite o número do mês'))

while n < 1 or n > 12:
    print ('inválido')
    n = int(input('Digite o número do mês'))
    
meses = ['janeiro','fevereiro','março','abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

nome_dos_meses = meses[n-1]

print(nome_dos_meses)