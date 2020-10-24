inicial = float(input())
mensal = float(input())
juros = float(input())
f = inicial + 24*mensal
i = 0

while i < 24:
    inicial += mensal + inicial*(juros)
    print("{:.2f}".format(inicial))
    i+=1
    
print("{:.2f}".format(inicial - f))
    
