inicial = float(input("Start"))
taxa = float(input("Taxa"))/100/12
final = inicial

i = 0
mes = 0

while i < 24:
    mes = incial*(1 + taxa)**i
    print("{0:.2f}".format(mes))
    i = i + 1

print("{0:.2f}".format(mes - inicial))