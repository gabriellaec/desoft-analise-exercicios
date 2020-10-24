ini = float(input("Qual o depósito inicial? "))
mens = float(input("Qual o depósito mensal? "))
juros = float(input("Qual a taxa de juros? "))
TOTAL = ini
i = 0
while i < 24:
    TOTAL *= 1 + juros
    print('{0:.2f}'.format(TOTAL))
    TOTAL += mens
    i += 1
print('{:.2f}'.format((TOTAL - ini - (23*mens))))