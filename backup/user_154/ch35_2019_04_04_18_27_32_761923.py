inicial = float(input("Start"))
mensal = float(input("Mensal"))
taxa = float(input("Taxa"))

i = 0

while i < 24:
    inicial = inicial*taxa + mensal
    print("{0:.2f}".format(incial))
    