ini = float(input("Qual o depósito inicial? "))
mens = float(input("Qual o depósito mensal? "))
juros = float(input("Qual a taxa de juros? "))
MESES = 24
TOTAL = ini
i = 0
while i < MESES:
    TOTAL *= 1 + juros
    print('{0:.2f}'.format(TOTAL))
    TOTAL += mens
    i += 1
print('{:.2f}'.format((TOTAL - ini - (MESES*mens))))