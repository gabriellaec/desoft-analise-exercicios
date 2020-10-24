inicial = float(input())
mensal = float(input())
taxa = float(input())
i = 1
total = inicial 
for i in range(24):
    inicial = inicial * (1+taxa) + mensal
    print(inicial) 
final = inicial - total - 24 * mensal
print(final)