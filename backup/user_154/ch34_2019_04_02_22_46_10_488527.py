inicial = float(input("Start"))
taxa = float(input("Taxa"))

taxa = 1 + taxa/100

i = 0

while i < 24:
    print(incial*taxa)
    incial = incial*taxa

print(inicial)