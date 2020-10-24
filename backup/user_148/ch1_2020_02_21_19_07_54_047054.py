v = float(input('Valor emprestado: '))

m = int(input('Número de meses: '))

t = float(input('Taxa de juros: '))

M = v*(1+t/100)**m

print(f'O valor devido é de: {M}')