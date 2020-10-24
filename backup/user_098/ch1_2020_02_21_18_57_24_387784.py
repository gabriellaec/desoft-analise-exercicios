ve = float(input("Valor Emprestado:"))

n = int(input("Meses de Empréstimo:"))

i = float(input("Taxa de Juros:"))

i = i/100

vt = ve * (1+i)**n

print('Valor Total: R$', vt)