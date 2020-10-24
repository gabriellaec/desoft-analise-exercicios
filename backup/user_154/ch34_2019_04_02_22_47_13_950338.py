inicial = float(input("Start"))
taxa = float(input("Taxa"))/100

i = 0

while i < 24:
    print(incial*taxa)
    incial = incial*(1+taxa)
    i = i + 1

print(inicial)