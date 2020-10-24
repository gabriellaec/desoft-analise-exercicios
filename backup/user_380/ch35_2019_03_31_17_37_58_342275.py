inicial = float(input())
mensal = float(input())
taxa = float(input())
total = inicial 
for i in range(24):
    inicial = inicial * (1+taxa) + mensal
    print("{0:.2f}".format(inicial)) 
print("{0:.2f}".format(inicial - total - 24 * mensal))
